from django.urls import path
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import SignUpView, user_profile_view

urlpatterns = [
	path('signup/', SignUpView.as_view(), name='signup'),
	path('user-profile/', user_profile_view, name='user-profile')

]

# urlpatterns += staticfiles_urlpatterns()