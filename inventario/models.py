from django.db import models
from django.core.validators import EmailValidator
from .validators import validar_email, validar_precio, validar_rating, validar_url, validar_nombre_no_comida


class Author(models.Model):
    first_name = models.CharField(max_length=100, validators=[validar_nombre_no_comida])
    last_name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator, validar_email])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Publisher(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[validar_nombre_no_comida])
    website = models.URLField(validators=[validar_url])

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_precio])
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    rating = models.PositiveIntegerField(validators=[validar_rating])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review of {self.book.title} by {self.book.author.first_name} {self.book.author.last_name}"
