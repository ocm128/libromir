from django.shortcuts import render
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

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
    template_name = 'catalog/book_list.html'


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


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    model = BookInstance
    paginate_by = 2

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(
            status__exact='o').order_by('due_back')


class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
    """
    Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission.
    """
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name ='catalog/bookinstance_list_borrowed_all.html'
    paginate_by = 2

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')