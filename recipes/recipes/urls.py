"""
URL configuration for recipes project.

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
from cookie import views

urlpatterns = [
	path('logout/', views.custom_logout, name="logout"),
	path('pdf/', views.pdf , name='pdf'),
	path('admin/', admin.site.urls),
	path('login/' , views.login_page, name='login'),
	path('register/', views.register_page, name='register'),
	
	path('', views.recipes, name='recipes'),
	path('update_recipe/<id>', views.update_recipe, name='update_recipe'),
	path('delete_recipe/<id>', views.delete_recipe, name='delete_recipe'),
]
