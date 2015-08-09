from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from forms import QuestionForm, PlayerForm
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
        print 'fuck'
        form = QuestionForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return questions(request)
        else: 
            print form.errors
    else:
        form = QuestionForm()

    return render(request, 'add_question.html', {'form' : form})

def start_game(request):
    context_dict = {}

    if request.method == 'POST':

        player1 = request.POST.get('player1', None)
        if player1:
            context_dict['player1'] = player1

        player2 = request.POST.get('player2', None)
        if player2:
            context_dict['player2'] = player2
        
        context_dict['form'] = PlayerForm(request.POST)
        return render(request, 'index.html', context_dict)

    context_dict['form'] = PlayerForm()
    return render(request, 'start_game.html', context_dict)


