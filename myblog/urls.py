"""myblog URL Configuration

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
from django.urls import path,include
from posts import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView


urlpatterns = [
    path('',views.index,name="index"),
    path('admin/', admin.site.urls),
    path('home/',views.home,name = "home"),
    path('home/<int:instance_id>/detail',views.detail,name = "detail"),
    path('home/<int:instance_id>/edit',views.edit,name='edit'),
    path('home/create',views.create,name="create"),
    path('signup/',views.signup , name = 'signup'),
    path('home/',TemplateView.as_view(template_name='home.html'),name='home'),
    path('',include('django.contrib.auth.urls')),
    path('home/<int:instance_id>/detail/delete',views.delete,name = "delete"),
    path('home/logout',views.logoutv,name = 'logoutv'),
    path('home/<int:instance_id>/detail/likes',views.likes,name = "likes"),
    path('home/profile',views.profile,name="profile"),
    path('home/profile/edit',views.edit_profile,name="edit_profile"),
    path('home/profie/password',views.change_password,name = "change_password"),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
