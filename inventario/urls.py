from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import AuthorViewSet, PublisherViewSet, BookViewSet, ReviewViewSet

# Crear un enrutador para DRF
router = DefaultRouter()
router.register(r"authors", views.AuthorViewSet)
router.register(r"publishers", views.PublisherViewSet)
router.register(r"books", views.BookViewSet)
router.register(r"reviews", views.ReviewViewSet)

urlpatterns = [

    # ---------- Para poder usar Django Rest Framework se comentó este bloque ----------
    # Rutas para autores
    # path('authors/', views.author_list, name='author_list'),
    # path('authors/<int:id>/', views.author_detail, name='author_detail'),
    # path('authors/form/', views.author_form_view, name='author_form'),

    # Rutas para editores (publishers)
    # path('publishers/', views.publisher_list, name='publisher_list'),
    # path('publishers/<int:id>/', views.publisher_detail, name='publisher_detail'),
    # path('publishers/form/', views.publisher_form_view, name='publisher_form'),

    # Rutas para libros (books)
    # path('books/', views.book_list, name='book_list'),
    # path('books/<int:id>/', views.book_detail, name='book_detail'),
    # path('books/form/', views.book_form_view, name='book_form'),

    # Rutas para reseñas (reviews)
    # path('reviews/', views.review_list, name='review_list'),
    # path('reviews/<int:id>/', views.review_detail, name='review_detail'),
    # path('reviews/form/', views.review_form_view, name='review_form'),
    # ---------- Para poder usar Django Rest Framework se comentó este bloque ----------


    # ---------- Para poder usar Custom API se comentó este bloque ----------
    # path('', include(router.urls)),
    # ---------- Para poder usar Custom API se comentó este bloque ----------


    path('authors/count/', views.author_count, name='author_count'),
    path('books/publisher/<int:publisher_id>/', views.books_by_publisher, name='books_by_publisher'),
    path('reviews/author/<int:author_id>/', views.reviews_by_author, name='reviews_by_author'),
    path('reviews/create/', views.create_review, name='create_review'),
    
]
