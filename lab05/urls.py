"""lab05 URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin

from servlet import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(servlet2/)?$', views.Servlet2View.as_view(), name='servlet2'),
    url(r'^servlet3/?$', views.Servlet3View.as_view(), name='servlet3'),
    url(r'^servlet5/?$', views.Servlet5View.as_view(), name='servlet5'),
    url(r'^servlet6/?$', views.Servlet6View.as_view(), name='servlet6'),
    url(r'^servlet7/?$', views.Servlet7View.as_view(), name='servlet7'),
    url(r'^logoff/?$', views.logoff, name='logoff'),
]
