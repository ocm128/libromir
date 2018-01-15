from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance, Genre

# Create your views here.

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    #Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count() # The 'all()' is implied by default

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context_dict = {'num_books': num_books, 'num_instances': num_instances}
    context_dict['num_instances_available'] = num_instances_available
    context_dict['num_authors'] = num_authors
    context_dict['num_visits'] = num_visits

    return render(request, 'index.html', context_dict)


class BookListView(generic.ListView):
    """
    Generic class-based view for a list of books.
    """
    model = Book
    paginate_by = 3

    # Name for the list as a template variable
    # By defect is the model name and '_list' or 'object_list'
    #context_object_name = 'my_book_list'

    # Get 5 books containing the title war
    #queryset = Book.objects.filter(title__icontains='war')[:5]

    # Specify the template name/location.
    # By defect is the model name and '_list.html'
    #template_name = 'books/my_arbitrary_template_name_list.html'


class BookDetailView(generic.DetailView):
    """
    Generic class-based detail view for a book.
    """
    model = Book


class AuthorListView(generic.ListView):
    """
    Generic class-based view for a list of authors.
    """
    model = Author
    paginate_by = 3


class AuthorDetailView(generic.DetailView):

    model = Author