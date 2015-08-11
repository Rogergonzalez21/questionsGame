from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from forms import QuestionForm
from models import Question
# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required
def questions(request):
    questions = Question.objects.all()
    return render(request, 'questions.html', {'questions' : questions})

@login_required
def add_question(request):

    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return questions(request)
        else: 
            print form.errors
    else:
        form = QuestionForm()

    return render(request, 'add_question.html', {'form' : form})

@login_required
def edit_question(request, question_id):

    question_to_edit = Question.objects.get(id=question_id)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question_to_edit)

        if form.is_valid():
            form.save()        
            return questions(request)
    else:
        form = QuestionForm(instance=question_to_edit)

    return render(request, 'add_question.html', {'form' : form})

def start_game(request):
    context_dict = {}
    questions = Question.objects.all()
    questions1 = Question.objects.filter(value=1)
    questions2 = Question.objects.filter(value=2)
    questions3 = Question.objects.filter(value=3)
    questions4 = Question.objects.filter(value=4)

    context_dict['questions1'] = questions1
    context_dict['questions2'] = questions2
    context_dict['questions3'] = questions3
    context_dict['questions4'] = questions4
    
    return render(request, 'start_game.html', context_dict)

def question_detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'question_detail.html', {'question' : question})



