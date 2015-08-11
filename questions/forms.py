#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from models import Values, Dificulty, Question 

class QuestionForm(forms.ModelForm):
	question = forms.CharField(max_length=128, help_text="Pregunta: ", widget=forms.TextInput(attrs={'class':'form-control'}))
	dificulty = forms.ModelChoiceField(queryset=Dificulty.objects.all(), help_text="Dificultad: ", widget=forms.Select(attrs={'class':'form-control'}))
	value = forms.ModelChoiceField(queryset=Values.objects.all(), help_text="Valor: ", widget=forms.Select(attrs={'class':'form-control'}))
	
	class Meta:
		model = Question
		fields = ('question','value',)