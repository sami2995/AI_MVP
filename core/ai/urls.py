from django.urls import path
from . import views

urlpatterns = [
    path('', views.subject_list, name='subject_list'),
    path('subjects/<int:subject_id>/topics/', views.topic_list, name='topic_list'),
    path('topics/<int:topic_id>/materials/', views.material_list, name='material_list'),
    path('quiz-results/', views.quiz_results, name='quiz_results'),
    path('quizzes/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
]
