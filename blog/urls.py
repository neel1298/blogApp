from django.urls import path
from .views import PostListView,PostDetailView
from . import views
urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('about/',views.about,name='blog-about'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/create/',views.createPost,name='create-post'),
    path('post/<int:pk>/update',views.updatePost,name='update-post'),
    path('post/<int:pk>/delete',views.deletePost,name='delete-post'),
    path('post/<int:id>/userpost',views.userPost,name='user-posts'),
    path('post/searchuser/',views.searchUser,name='search-user')
]
