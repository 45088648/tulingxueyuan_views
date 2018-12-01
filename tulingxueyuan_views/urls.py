"""tulingxueyuan_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from teacher_app import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^teacher/', v.teacher, name="t"),
    url(r'^teacher1/', v.teacher1),
    url(r'^v9_get/', v.v9_get),
    url(r'^v9_post/', v.v9_post),
    url(r'^ttt/', v.ttt),
    url(r'^render_test/', v.render_test),
    url(r'^toolingInfo/', v.toolingInfo),
    url(r'^ti/', v.ToolingInfoListView.as_view(), name="toolingInfo-list"),
    url(r'^simpleemail/', v.sendSimpleEmail),
    url(r'^t_exception/', v.t_exception)
]
