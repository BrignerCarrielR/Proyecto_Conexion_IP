"""
URL configuration for principal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from monitoreo.views import InicioTemplateView, List_swicth_View, New_swicth_View, Update_Switch_View, \
    Delete_Switch_View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InicioTemplateView.as_view(), name="inicio"),
    path('list_swicth_View', List_swicth_View.as_view(), name="list_swicth_View"),
    path('new_swicth_View', New_swicth_View.as_view(), name="new_swicth_View"),
    path('update_Switch_View/<int:pk>', Update_Switch_View.as_view(), name="update_Switch_View"),
    path('delete_Switch_View/<int:pk>', Delete_Switch_View.as_view(), name="delete_Switch_View"),
]
