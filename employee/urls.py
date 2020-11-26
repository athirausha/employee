"""employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from emp import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index',views.fn_index),
    path('login',views.fn_login),
    path('add_employee',views.load_addemployee),
    path('view_employee',views.view_employee),
    path('load_dashboard',views.load_dashboard),
    path('chartdata_fetch', views.Chartdata_fetch),
    path('update_data', views.update_employee),
    path('logout', views.Logout),
    path('data_image_upload', views.data_image_upload),
    path('delete_data',views.Delete_data),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL,
                                                                         document_root=settings.MEDIA_ROOT)
