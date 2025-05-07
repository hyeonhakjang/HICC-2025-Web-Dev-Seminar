"""
URL configuration for hicc_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from hicc_project.views import text_tag_render, html_test_render, image_tag_render, form_tag_render, table_tag_render, \
    layout_tag_render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('html_test/', html_test_render),
    path('text_tag/', text_tag_render),
    path('image_tag/', image_tag_render),
    path('form_tag/', form_tag_render),
    path('table_tag/', table_tag_render),
    path('layout_tag/', layout_tag_render),
]
