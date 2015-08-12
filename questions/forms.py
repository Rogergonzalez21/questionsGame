#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.forms.models import modelformset_factory
from models import Values, Dificulty, Question 

class QuestionForm(forms.ModelForm):
	question = forms.CharField(max_length=128, label="Pregunta: ", widget=forms.TextInput(attrs={'class':'form-control'}))
	dificulty = forms.ModelChoiceField(queryset=Dificulty.objects.all(), label="Dificultad: ", widget=forms.Select(attrs={'class':'form-control'}))
	value = forms.ModelChoiceField(queryset=Values.objects.all(), label="Valor: ", widget=forms.Select(attrs={'class':'form-control'}))
	
	class Meta:
		model = Question
		fields = ('question','value',)

question_label = {'question' : "Pregunta", 'dificulty' : "Dificultad", 'value' : "Valor"}

QuestionFormSet = modelformset_factory(Question, fields=('question', 'dificulty', 'value'), extra=1, 
	widgets={'question': forms.TextInput(attrs={'class':'form-control'}), 
	'dificulty' : forms.Select(attrs={'class':'form-control'}), 
	'value' : forms.Select(attrs={'class':'form-control'})}, labels=question_label)