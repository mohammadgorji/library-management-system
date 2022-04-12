from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from rest_framework.views import APIView
from rest_framework.response import Response

from datetime import datetime, date, timedelta
from book.forms import RenewBookForm

from .models import Author
from .models import Book
from .models import BookInstance
from .models import Genre

from .serializer import BookSerializer


@login_required
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()
    num_author = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_author': num_author,
    }
    return render(request, 'book/index.html', context)


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    paginate_by = 3

    redirect_fiels_name = ''

    '''
    #login_url = 'accounts/login/'
    #template_name = "book_list.html"
    #context_object_name = "book_list"
    #query = Book.objects.filter(title__icontains='django')[:5]

    def get_queryset(self):
        return Book.objects.filter(title__icontains='farm')[:5]

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)

        context['my_book_list'] = Book.objects.all()

        return context
    '''


class LoanedBookListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'book/borrowed_list.html'
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book
    template_name = "book/book_detail.html"

    redirect_fiels_name = ''


'''
    login_url = 'accounts/login/'
def book_detail_view(request, pk):
    try:
        book_id = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404('Book does not exist.')
    #book_id = get.object_or_404(Book, pk = pk)

    return render(request, 'book/book_detail.html', context={'book': book_id})
'''


class LoanedBookByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'book/bookinstance_list_borrower_user.html'
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


@login_required
@permission_required('book.librarian')
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    if request.method == 'POST':

        form = RenewBookForm(request.POST)

        if form.is_valid():
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            return HttpResponseRedirect(reverse_lazy('book:allBorrowed'))

    else:
        proposed_renewal_date = date.today() + timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'book/book_renew_librarian.html', context)


class APIListBook(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data)
