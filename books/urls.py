#books urls 

from django.urls import path
from . import views


urlpatterns = [
  path('', views.index),
  path('add_books', views.add_books),
  path('<int:book_id>', views.book_details),
  path('fav/<int:book_id>', views.fav),
  path('un_favorite/<int:book_id>', views.un_favorite),
  path('update_book/<int:book_id>', views.update_book),
  path('delete_book/<int:book_id>', views.delete_book)
]