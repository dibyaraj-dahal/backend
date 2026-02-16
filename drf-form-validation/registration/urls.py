from django.urls import path
from . import views

app_name = 'registration'

# urlpatterns = [
#     path('', views.RegistrationListAPIView.as_view(), name="registration")
# ]
urlpatterns = [
    # name='form' is required
    path('form/', views.registration_form, name='form'),
]
