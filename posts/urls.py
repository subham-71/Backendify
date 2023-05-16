from django.urls import path
from posts import views

urlpatterns =[
    path('posts/',views.PostView.as_view()),
    path('posts/<chapterName>',views.selectedView.as_view()),
    path('posts/id/<id>',views.idView.as_view()),
    path('posts/likes/id/<id>',views.LikesDislikesView.as_view()),
    path('posts/delete-post/<id>',views.DeletePostView.as_view()),
]