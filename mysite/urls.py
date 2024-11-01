"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # Updated to use path instead of url
from django.contrib.auth import views as auth_views  # Proper import for auth views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # No change needed for include
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Updated to use class-based view
    #path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),  # Updated to use class-based view
    #path('accounts/logout/',views.log_views,name='logout'),  # Updated to use class-based view
]
