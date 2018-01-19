from django.conf.urls import include, url

from . import views


urlpatterns = [

    #url('', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'books/$', views.BookListView.as_view(), name='books'),
    #url('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    url(r'book/(?P<pk>[\w\-]+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'authors', views.AuthorListView.as_view(), name='authors'),
    url(r'author/(?P<pk>[\w\-]+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'mybooks', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url(r'borrowed', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
    url(r'book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]