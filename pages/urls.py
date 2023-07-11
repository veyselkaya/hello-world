from django.urls import path
from .views import homPageView

urlpatterns = [
    path('', homPageView, name='home')
]
