from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, filters, generics
from django_filters.rest_framework import DjangoFilterBackend


# we create our endpoints here. These are for accessing data
'''
Serializers are classes that allow complex data types,
such as Django querysets and model instances, 
to be converted into native Python data types,
which can then be easily rendered into JSON, XML, or other content types for APIs.
'''


@api_view(['GET', 'POST']) # this decorator describes how the function should work
def book_list(request):
    # get book list, serialize them and return json file
    if request.method == 'GET':
        books = Library.objects.all()
        serializer = Library_Serializer(books, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK )
    if request.method == 'POST':
        serializer = Library_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
        # Return errors if the serializer data is invalid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])     
def book_details(request,id):

    try:
        book = Library.objects.get(pk=id)
    except Library.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = Library_Serializer(book)
        return Response(serializer.data,  status = status.HTTP_200_OK )
    
    elif request.method == 'PUT':
        serializer = Library_Serializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# def get_book(request):
#     if request.method== 'GET':
#         # books = Library.objects.all()
#         author = request.GET.get('book_author')
#         if author is not None:
#                 books = books.filter(book_author__iexact=author)
#         serializer = Library_Serializer(books, many=True)
#         return Response(serializer.data,  status = status.HTTP_200_OK )


# filter_backends = [DjangoFilterBackend]
# filterset_fields = ['book_author', 'book_title']

class BookListView(generics.ListAPIView):
    queryset = Library.objects.all()
    serializer_class = Library_Serializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['book_author', 'book_title']

