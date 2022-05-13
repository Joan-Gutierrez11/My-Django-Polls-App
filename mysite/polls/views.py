from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from polls.models import *
from django.urls import reverse
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'questions_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[0:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def index(request):
#     questions_list = Question.objects.order_by('-pub_date')[0:10]
#     output = ', '.join([q.question_text for q in questions_list])
#     ctx = {'questions_list': questions_list}
#     return render(request, 'polls/index.html', ctx)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request:HttpRequest, question_id):
#     question = get_object_or_404(Question, pk=question_id)    
#     return render(request, 'polls/results.html', {'question':question})

def vote(request:HttpRequest, question_id):
    question = Question.objects.get(pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id, )))