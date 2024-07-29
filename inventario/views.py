from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Author, Publisher, Book, Review
from .forms import AuthorForm, PublisherForm, BookForm, ReviewForm
from .serializers import AuthorSerializer, PublisherSerializer, BookSerializer, ReviewSerializer
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Vistas para autores
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def author_detail(request, id):
    author = get_object_or_404(Author, id=id)
    return render(request, 'author_detail.html', {'author': author})

def author_form_view(request):
    form = AuthorForm(request.POST or None)
    author = None
    id_author = request.GET.get("id")
    if id_author:
        author = get_object_or_404(Author, id=id_author)
        form = AuthorForm(instance=author)

    if request.method == "POST":
        if author:
            form = AuthorForm(request.POST, instance=author)
        else:
            form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()

    return render(request, "form_authors.html", {"form": form})

# Vistas para editores (publishers)
def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publishers': publishers})

def publisher_detail(request, id):
    publisher = get_object_or_404(Publisher, id=id)
    return render(request, 'publisher_detail.html', {'publisher': publisher})

def publisher_form_view(request):
    form = PublisherForm(request.POST or None)
    publisher = None
    id_publisher = request.GET.get("id")
    if id_publisher:
        publisher = get_object_or_404(Publisher, id=id_publisher)
        form = PublisherForm(instance=publisher)

    if request.method == "POST":
        if publisher:
            form = PublisherForm(request.POST, instance=publisher)
        else:
            form = PublisherForm(request.POST)

        if form.is_valid():
            form.save()

    return render(request, "form_publishers.html", {"form": form})

# Vistas para libros (books)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'book_detail.html', {'book': book})

def book_form_view(request):
    form = BookForm(request.POST or None)
    book = None
    id_book = request.GET.get("id")
    if id_book:
        book = get_object_or_404(Book, id=id_book)
        form = BookForm(instance=book)

    if request.method == "POST":
        if book:
            form = BookForm(request.POST, instance=book)
        else:
            form = BookForm(request.POST)

        if form.is_valid():
            form.save()

    return render(request, "form_books.html", {"form": form})

# Vistas para reseñas (reviews)
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})

def review_detail(request, id):
    review = get_object_or_404(Review, id=id)
    return render(request, 'review_detail.html', {'review': review})

def review_form_view(request):
    form = ReviewForm(request.POST or None)
    review = None
    id_review = request.GET.get("id")
    if id_review:
        review = get_object_or_404(Review, id=id_review)
        form = ReviewForm(instance=review)

    if request.method == "POST":
        if review:
            form = ReviewForm(request.POST, instance=review)
        else:
            form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()

    return render(request, "form_reviews.html", {"form": form})

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


@api_view(['GET'])
def author_count(request):
    """
    Cuenta la cantidad de autores
    """
    try:
        cantidad = Author.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )

@api_view(['GET'])
def books_by_publisher(request, publisher_id):
    """
    Lista de libros filtrados por un editor (publisher)
    """
    try:
        books = Book.objects.filter(publisher_id=publisher_id)
        return JsonResponse(
            BookSerializer(books, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )

@api_view(['GET'])
def reviews_by_author(request, author_id):
    """
    Lista de reseñas por autor
    """
    try:
        books = Book.objects.filter(author_id=author_id)
        reviews = Review.objects.filter(book__in=books)
        return JsonResponse(
            ReviewSerializer(reviews, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )

@api_view(['POST'])
def create_review(request):
    """
    Crear una nueva reseña
    """
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"mensaje": "Reseña creada"}, status=201)
    else:
        return JsonResponse(serializer.errors, status=400)