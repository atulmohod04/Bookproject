"""bookproject URL Configuration

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
from bookinfo.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', homepage),
    path('save_book_info/', save_book_info),
    path('delete_data/<int:id>/', delete_data),
    path('edit_book/<int:id>/', edit_book),
    path('show_deleted_book/', show_deleted_book),
    path('restore/<int:id>/', restore_book),

    # path("register/<int:id>/", register_request, name="register"),
    path("register/", register_request,name="register"),
    path("login/", login_request, name="login"),
    path("landing_page/", landing_page, name="landing_page"),
    path("logout/", logout_request, name= "logout"),
    path("user_info/", user_info, name= "user_info"),






]
