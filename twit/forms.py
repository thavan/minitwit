from django import forms
from accounts.models import CustomUser

class NewTweetForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ['first_name', 'last_name', 'email', 'age', 'bio']