from django.urls import path
from . import views

urlpatterns = [
    # Public views
    path('', views.subject_list, name='subject_list'),
    path('subjects/<int:subject_id>/topics/', views.topic_list, name='topic_list'),
    path('topics/<int:topic_id>/materials/', views.material_list, name='material_list'),
    path('quiz-results/', views.quiz_results, name='quiz_results'),
    path('quizzes/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    
    # Subject CRUD
    path('admin/subjects/', views.subject_admin, name='subject_admin_url'),
    path('admin/subjects/edit/<int:subject_id>/', views.subject_edit, name='subject_edit_url'),
    path('admin/subjects/delete/<int:subject_id>/', views.delete_subject, name='delete_subject_url'),
    
    # Topic CRUD
    path('admin/topics/', views.topic_admin, name='topic_admin_url'),
    path('admin/topics/edit/<int:topic_id>/', views.topic_edit, name='topic_edit_url'),
    path('admin/topics/delete/<int:topic_id>/', views.delete_topic, name='delete_topic_url'),
    
    # Material CRUD
    path('admin/materials/', views.material_admin, name='material_admin_url'),
    path('admin/materials/edit/<int:material_id>/', views.material_edit, name='material_edit_url'),
    path('admin/materials/delete/<int:material_id>/', views.delete_material, name='delete_material_url'),
    
    # Quiz CRUD
    path('admin/quizzes/', views.quiz_admin, name='quiz_admin_url'),
    path('admin/quizzes/edit/<int:quiz_id>/', views.quiz_edit, name='quiz_edit_url'),
    path('admin/quizzes/delete/<int:quiz_id>/', views.delete_quiz, name='delete_quiz_url'),
]
