from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from polls.models import Question

# Create your views here.

def index(request):
    questions_list = Question.objects.order_by('-pub_date')[0:10]
    output = ', '.join([q.question_text for q in questions_list])
    ctx = {'questions_list': questions_list}

    return render(request, 'polls/index.html', ctx)

def details(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)        
    # except:
    #     raise Http404('Question does not exists')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)