"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myapp/', include('myapp.urls')),
    url(r'^accounts/login/$', 'myproject.views.login'),
    url(r'^accounts/auth/$', 'myproject.views.auth_view'),
    url(r'^accounts/logout/$', 'myproject.views.logout'),
    url(r'^accounts/loggedin/$', 'myproject.views.loggedin'),
    url(r'^accounts/invalid/$', 'myproject.views.invalid_login'),

    url(r'^accounts/create_user/$', 'myproject.views.create_user'),
    url(r'^accounts/create_user_success/$', 'myproject.views.create_user_success'),
    
    url(r'^$', RedirectView.as_view(url='/myapp/list/', permanent=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)