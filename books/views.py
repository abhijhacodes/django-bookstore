from django.shortcuts import redirect
from books.models import Book, Review
from django.views.generic import ListView, DetailView


class BookListView(ListView):
    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-createdAt')
        return context


def review(request, id):
    body = request.POST['review']
    review = Review(body=body, book_id=id)
    review.save()
    return redirect('/book')
