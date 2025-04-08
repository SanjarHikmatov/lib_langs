"""
URL configuration for config project.

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
from importlib.metadata import requires

from django.contrib import admin
from django.urls import path
from django.conf.urls.i18n import i18n_patterns


from apps.books.views import (
    BookCreateView,
    BookListView,
    BookUpdateView,
    BookDeleteView)
from apps.books.middelware import translation

lang = translation.get_language()
urlpatterns = [
    path('admin/', admin.site.urls),

]
urlpatterns += i18n_patterns(
    path('', BookListView.as_view(), name='book-list'),
    path('create/', BookCreateView.as_view(), name='book-create'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
)
