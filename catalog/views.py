from django.shortcuts import render
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

    context_dict = {'num_books': num_books, 'num_instances': num_instances}
    context_dict['num_instances_available'] = num_instances_available
    context_dict['num_authors'] = num_authors

    return render(request, 'index.html', context_dict)

