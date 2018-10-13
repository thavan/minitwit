from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import SignUpForm

class SignUp(CreateView):
	form_class = SignUpForm
	template_name = 'registration/signup.html'
	success_url = reverse_lazy('login')


