from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.project, name='project'),
    path('project/<str:p_id>', views.detail_project, name='detail_project'),
]
