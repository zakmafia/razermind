from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.project, name='project'),
    path('project/<str:p_id>', views.detail_project, name='detail_project'),
    path('project/insert_image/<str:p_id>',
         views.insert_project_image, name='insert_project_image')
]
