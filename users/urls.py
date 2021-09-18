from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('accounts/register/', user_views.register, name ='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name = 'profile'),

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
