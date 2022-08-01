from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
	data = {}

	return render(request, 'pages/dashboard.html', data)

@login_required
def manage_passwords(request):
	data = {}

	return render(request, 'pages/manage_passwords.html', data)