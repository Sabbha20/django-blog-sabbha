from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomepageListView.as_view(), name='homepage'),
    path('post/<int:pk>', views.PostDetailsView.as_view(), name='post_detail'),
    path('post/create', views.PostCreateView.as_view(), name='post_create'),
    path('post/update/<int:pk>', views.PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>', views.PostDeleteView.as_view(), name='post_delete'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
]
