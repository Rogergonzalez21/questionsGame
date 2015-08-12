from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from forms import QuestionForm, QuestionFormSet
from models import Question, Dificulty
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
        formset = QuestionFormSet(request.POST, request.FILES)

        if formset.is_valid():
            formset.save(commit=True)
            return questions(request)
        else: 
            print formset.errors
    else:
        formset = QuestionFormSet()

    return render(request, 'add_question.html', {'formset' : formset})

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

def delete_question(request, question_id):

    if request.method == 'POST':
        delete(request, question_id)
        return questions(request)

    return render(request, 'delete_question.html', {'question' : Question.objects.get(id=question_id)})

def right_question(request, dificulty_id, question_id):

    if request.method == 'POST':
        delete(request, question_id)
        return game(request, dificulty_id)

    return render(request, 'right.html')

def wrong_question(request, dificulty_id, question_id):

    if request.method == 'POST':
        delete(request, question_id)
        return game(request, dificulty_id)

    return render(request, 'wrong.html')

def start_game(request):

    dificulty = Dificulty.objects.all()
    return render(request, 'dificulty.html', {'dificulty' : dificulty})


def game(request, dificulty_id):
    context_dict = {}
    questions = Question.objects.all()
    questions1 = Question.objects.filter(value=1, dificulty=dificulty_id)
    questions2 = Question.objects.filter(value=2, dificulty=dificulty_id)
    questions3 = Question.objects.filter(value=3, dificulty=dificulty_id)
    questions4 = Question.objects.filter(value=4, dificulty=dificulty_id)

    context_dict['questions1'] = questions1
    context_dict['questions2'] = questions2
    context_dict['questions3'] = questions3
    context_dict['questions4'] = questions4
    
    return render(request, 'game.html', context_dict)

def question_detail(request, dificulty_id, question_id):
    question = Question.objects.get(id=question_id, dificulty=dificulty_id)
    return render(request, 'question_detail.html', {'question' : question})


def delete(request, question_id):

    question_to_delete = Question.objects.get(id=question_id)
    question_to_delete.delete()


