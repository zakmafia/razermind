from django.urls import path
from . import views

urlpatterns = [
    path('blog/<str:b_id>', views.detail_blog, name='detail_blog'),
]
