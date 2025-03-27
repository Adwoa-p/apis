import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  
    author = django_filters.CharFilter(lookup_expr='icontains')  
    # created_at = django_filters.DateFromToRangeFilter() 

    class Meta:
        model = Book
        fields = ['book_title', 'book_author']
