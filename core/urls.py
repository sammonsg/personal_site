from django.urls import path

from . import views

urlpatterns = [
    path('', views.WorkInProgressView.as_view(), name='wip'),
    path('home/', views.HomepageView.as_view(), name='home')
]
