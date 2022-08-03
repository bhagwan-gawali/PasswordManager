from django.urls import path
from .views import (
		dashboard_view, manage_passwords, all_passwords, update_password,
		delete_password, all_cards, update_card, delete_card, all_trash,
		restore_pass, restore_card
	)

urlpatterns = [
	path('dashboard/', dashboard_view, name='dashboard'),
	path('manage-passwords/', manage_passwords, name='manage-passwords'),
	path('all-passwords/', all_passwords, name='all-passwords'),
	path('update-password/', update_password, name='update-password'),
	path('delete-password/', delete_password, name='delete-password'),
	path('all-cards/', all_cards, name='all-cards'),
	path('update-card/', update_card, name='update-card'),
	path('delete-card/', delete_card, name='delete-card'),
	path('all-trash/', all_trash, name='all-trash'),
	path('restore-pass/<int:pass_id>/', restore_pass, name='restore-pass'),
	path('restore-card/<int:card_id>/', restore_card, name='restore-card'),
]