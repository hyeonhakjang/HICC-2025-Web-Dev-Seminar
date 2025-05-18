from django.urls import path
from . import views

urlpatterns = [
    path('question/<int:question_id>/', views.question_detail),
    path('question/', views.questions),
    path('question/<int:question_id>/answer', views.answers)
]