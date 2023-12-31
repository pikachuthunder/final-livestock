
from django.conf import settings
#from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Add the following line at the end of your urlpatterns



urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup, name="signup"),
    path('home', views.home, name="home"),
    path('logout/', views.logout_view, name="logout"),   
    path('add/', views.add, name="add"),  
    path('delete/<int:id>/', views.delete_view, name="delete"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('upload_display_video/', views.upload_display_video, name="upload_display_video"),
    path('profile/', views.profile, name='profile'),
    path('upload/', views.upload_video, name='upload_video'),
    # path('list/', views.video_list, name='video_list'),
    path('video/<int:video_id>/', views.video_detail, name='video_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)