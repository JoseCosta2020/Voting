from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question, Choice

# Create your views here.
def QuestionTeste(request):
    return HttpResponse('Ole')

#Goodo
def Goods(request):
    return HttpResponse('OLELLE')

def Goods2(request):
    return HttpResponse('OLELLEhhhhhhh')

#Get Question and display questions
def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    print('Latest:',latest_question_list)
    context= {'latest_question_list':latest_question_list}
    print('Context',context)
    return render(request, 'index.html', context)
    
#Show question and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        context = {'question':question}
    except Question.DoesNotExist:
        return 'Id  not exist'
    return render(request, 'detail.html', context)    
       
#Get question and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'results.html',{'question':question})

# Vote for a qerstion choice
def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', 
                      { 'question': question,
                        'error_message': 'You did not select a choice.'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))