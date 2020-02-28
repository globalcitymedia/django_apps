# posts/urls.py
from django.urls import path
from . import views
# from .views import HomePageView

app_name = 'libraryapp'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('/create', views.upload, name='create'),
    # ex: /polls/5/results/
    path('<int:book_id>', views.update_book, name='update'),
    # ex: /polls/5/vote/
    path('<int:book_id>', views.delete_book, name='delete'),
]