from django.urls import path
from . import views

urlpatterns = [
    # path('upload-project', views.upload_project, name='upload_project'),  
    path('project/<str:p_id>', views.detail_project, name='detail_project'), 
]
