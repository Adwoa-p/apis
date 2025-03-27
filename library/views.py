from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django.core.paginator import Paginator
from django_filters.rest_framework import DjangoFilterBackend
from library.pagination import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import *
from .filters import BookFilter

# we create our endpoints here. These are for accessing data
'''
Serializers are classes that allow complex data types,
such as Django querysets and model instances, 
to be converted into native Python data types,
which can then be easily rendered into JSON, XML, or other content types for APIs.
'''

# get all books from db
class BookListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'size'
    max_page_size = 5

@api_view(['GET']) 
def all_books(request):
    books = Book.objects.all().order_by('book_title')
    
    # search filtering
    search_filter = filters.SearchFilter()
    books = search_filter.filter_queryset(request, books, view=None)

    books = BookFilter(request.GET, queryset=books).qs

    # pagination
    paginator = BookListPagination()
    result_page = paginator.paginate_queryset(books, request)

    serializer = Library_Serializer(books, many=True)
    return paginator.get_paginated_response(serializer.data)

# add books to db
@api_view(['POST']) # this decorator describes how the function should work
@permission_classes([IsAdminUser])
def book_list(request):
    # get book list, serialize them and return json file
 if request.method == 'POST':
    serializer = Library_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get a particular book by id
@api_view(['GET'])     
def book(request,id):

    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = Library_Serializer(book)
        return Response(serializer.data,  status = status.HTTP_200_OK )

# update book details and delete book from db
@api_view(['PUT', 'DELETE']) 
@permission_classes([IsAdminUser])
def book_updates(request,id):
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = Library_Serializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.is_deleted = True
        return Response({"message":"Book successfully deleted"},status=status.HTTP_204_NO_CONTENT)









