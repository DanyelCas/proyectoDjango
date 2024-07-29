from django.contrib import admin
from .models import Author, Publisher, Book, Review

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'email')
    list_display = ('first_name', 'last_name', 'email')
    ordering = ('last_name', 'first_name')

class PublisherAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'website')
    ordering = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'publication_date', 'price', 'available')
    list_filter = ('author', 'publisher', 'available')
    search_fields = ('title', 'author__first_name', 'author__last_name', 'publisher__name')
    ordering = ('publication_date',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'rating', 'created')
    list_filter = ('rating',)
    search_fields = ('book__title', 'review_text')
    ordering = ('-created',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
