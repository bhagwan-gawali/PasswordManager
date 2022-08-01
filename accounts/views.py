from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

from django.contrib.auth.decorators import login_required

class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'
		


@login_required
def user_profile_view(request):
	data = {}

	return render(request, 'accounts/pages/user_profile.html', data)

	