# flipkart/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from electronics import views as electronics_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1. The root path now goes to the LOGIN page.
    path('', auth_views.LoginView.as_view(template_name='electronics/login.html'), name='login'),
    
    # 2. The SIGNUP page is now at /signup/.
    path('signup/', electronics_views.signup_view, name='signup'),
    
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    
    # Your home/dashboard path remains the same
    path("home/", include("electronics.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)