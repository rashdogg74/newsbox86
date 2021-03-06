from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView,\
 DeletePostView, CategoryView, LikeView, AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>', CategoryView, name='category'),
    path('up_vote/<int:pk>', LikeView, name='up_vote'),
    path('post/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
]