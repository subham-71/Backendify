from authentication import views
from django.urls import path

urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name="register"),
    path('update-profile/<email>',
         views.UpdateProfileView.as_view(), name="update-profile"),

    path('login', views.LoginAPIView.as_view(), name="login"),
    path('super-register', views.SuperRegisterAPIView.as_view(),
         name="super-register"),
    path('forgot-password', views.ChangePasswordView.as_view(),
         name="forgot-pass"),

    path('delete-user', views.DeleteUserView.as_view(),
         name="forgot-pass"),

    path('all-users/<email>', views.UserEmailView.as_view(),
         name="all-users-email"),

    path('all-users', views.AllUsersView.as_view(),
         name="all-users"),
]
