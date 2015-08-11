#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
import models

class QuestionForm(forms.ModelForm):
	question = forms.CharField(max_length=128, help_text="Pregunta: ", widget=forms.TextInput(attrs={'class':'form-control'}))
	value = forms.ModelChoiceField(queryset=models.Values.objects.all(), help_text="Valor: ", widget=forms.Select(attrs={'class':'form-control'}))
	
	class Meta:
		model = models.Question
		fields = ('question','value',)