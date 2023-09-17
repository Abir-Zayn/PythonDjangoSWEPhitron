from django.urls import path
from book.views import *


urlpatterns = [
    path('',home, name='homepage'),
    path('store_new_book/',store_book, name="storebook"),
    path('show_books/', show_books, name='showbook'),
    path('edit_book/<int:id>',edit_book, name='editbook'),
    path('delete_book/<int:id>',delete_book, name='deletebook'),
]
