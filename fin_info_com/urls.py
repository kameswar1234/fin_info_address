"""fin_info_com URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from fin_info_com import settings
# from app1.views import index,create_data
from app1.views import Employe_Api
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employe_api/<int:pk>/',Employe_Api.as_view(),name='employe_api'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
