from django.urls import path
from .views import (
		dashboard_view, manage_passwords
	)

urlpatterns = [
	path('dashboard/', dashboard_view, name='dashboard'),
	path('manage-passwords/', manage_passwords, name='manage-passwords'),
	
]