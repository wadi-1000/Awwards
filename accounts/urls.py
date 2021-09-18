from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # login/signup &logout
    path('register/', views.register, name='register'),
    path('viewer_register/', views.viewer_register.as_view(), name='viewer_register'),
    path('employee_register/', views.employee_register.as_view(), name='employee_register'),
    path('', views.login_request, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # password reset
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
         name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_"
                                                                                        "sent.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name=
                                                                                "registration/password_reset.html"),
         name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password"
                                                                                                "_reset_done.html")
         , name='password_reset_complete'),
]