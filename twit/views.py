from django.shortcuts import render
from django.shortcuts import redirect
from accounts.models import CustomUser
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator
from django.urls import reverse

from .models import Message, Follow
from .forms import NewTweetForm, ProfileUpdateForm

from django.db.utils import IntegrityError

def home(request):
	if request.user.is_authenticated:
		return redirect(reverse('dashboard', args=(1,)))
	return render(request, 'home.html', {})

def dashboard(request, page):
	if request.user.is_authenticated:
		if request.method == 'POST':
			new_tweet = NewTweetForm(request.POST)
			# import pdb; pdb.set_trace();
			if new_tweet.is_valid():
				m = Message(**new_tweet.cleaned_data)
				m.author = request.user
				m.save()
				return redirect(reverse('dashboard', args=(1,)))
		else:
			new_tweet = NewTweetForm()
			users = CustomUser.objects.filter(~Q(username=request.user.username))
			follows = Follow.objects.filter(who=request.user)
			authors = []
			for follow in follows:
				authors.append(follow.whom)
			tweets = Message.objects.filter(author__in=authors)
			tweets_page = Paginator(tweets, 10)
			tweets = tweets_page.get_page(page)
			return render(request, 'dashboard.html', {'form': new_tweet, 'users': users, 
				'current_page': page, 'tweets': tweets})
	else:
		return redirect('home')


def user_dashboard(request, user):
	if request.user.is_authenticated:
		user_obj = User.objects.get(username=user)
		tweets = Message.objects.filter(author=user_obj.pk)
		return render(request, 'user_dashboard.html', {'tweets': tweets})
	else:
		return redirect('home')

def follow(request, user_id):
	if request.user.is_authenticated:
		if request.method=='POST':
			who = request.user
			whom = CustomUser.objects.get(pk=user_id)
			try:
				Follow.objects.create(who=who, whom=whom)
			except IntegrityError as e:
				return HttpResponse('Already Following')
			return HttpResponse('Following')
	else:
		redirect('home')


class ProfileUpdate(UpdateView):
	template_name = 'profile.html'
	form_class = ProfileUpdateForm
	model = CustomUser

	def get_context_data(self, **kwargs):
		tweets = Message.objects.filter(author=self.request.user)
		context = super(ProfileUpdate, self).get_context_data(**kwargs)
		context.update({'tweets': tweets})
		return context