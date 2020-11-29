from django.urls import path,re_path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('',views.Blog_PostListView.as_view(),name='all'),
    path('new/',views.CreatePost.as_view(),name='create'),
    re_path(r'^details/(?P<pk>\d+)/$',views.Blog_PostDetail.as_view(),name='post_det'),
    path('delete/<pk>',views.DeletePost.as_view(),name='delete'),
    
]