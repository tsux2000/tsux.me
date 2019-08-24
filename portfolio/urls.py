from django.urls import path
from .views import IndexView
from django.views.generic import TemplateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
