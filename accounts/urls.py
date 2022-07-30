from django.urls import path
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import SignUpView

urlpatterns = [
	path('signup/', SignUpView.as_view(), name='signup'),

]

# urlpatterns += staticfiles_urlpatterns()