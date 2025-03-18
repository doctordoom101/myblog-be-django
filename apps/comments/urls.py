from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('post/<int:post_id>/', views.CommentListView.as_view(), name='list'),
    path('create/', views.CommentCreateView.as_view(), name='create'),
    path('<int:pk>/', views.CommentUpdateDeleteView.as_view(), name='edit'),
]