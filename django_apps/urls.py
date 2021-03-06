"""django_apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from todoapp.views import index
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    url(r'^$', index, name="TodoList"),
    path('library', include('libraryapp.urls')),
]

# to view the img in development env
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)