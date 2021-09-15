from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Avg, Min,Max

from .models import Books

def index(request):
    books = Books.objects.all().order_by('-rating')
    number_of_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))
    # avg_rating = books.aggregate(Avg('rating'),Min('rating'),Max('rating')) # this returns a dictionary
    context = {'books': books, 'num_book':number_of_books, 'avg_rating':avg_rating}
    return render(request, 'book_store/index.html', context)

def detail(request,slug):    
    # book = get_object_or_404(Books, pk=id)
    book = get_object_or_404(Books, slug=slug)
    context = {'book': book}
    return render(request,'book_store/book_detail.html',context )

