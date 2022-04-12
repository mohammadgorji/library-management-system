from django.urls import path, re_path

from . import views

app_name = 'book'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.BookListView.as_view(), name='bookList'),
    path('detail/<int:pk>/', views.BookDetailView.as_view(), name='bookDetail'),
    path('mybooks/', views.LoanedBookByUserListView.as_view(), name='myBooks'),
    path('borrowed/', views.LoanedBookListView.as_view(), name='allBorrowed'),
    path('<int:pk>/renew/', views.renew_book_librarian,
         name='renewBookLibrarian'),
    re_path(r'^get/', views.APIListBooks.as_view(), name='apibooks')
]
