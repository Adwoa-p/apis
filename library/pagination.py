from rest_framework.pagination import *

class BookListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'size'
    max_page_size = 3


# class BookListPagination(CursorPagination):
#     page_size = 2
#     ordering = 'book_title'
#     cursor_query_param = 'record'


# class BookListPagination(LimitOffsetPagination):
#     default_limit = 2
#     max_limit = 2


# Custom pagination with PageNumberPagination
# class BookListPagination(PageNumberPagination):
#     page_size = 2
#     max_page_size = 3
#     page_size_query_param = 'size'

#     def get_paginated_response(self, data):
#         return Response({
#             'links': {
#                 'next': self.get_next_link(),
#                 'previous': self.get_previous_link()
#             },
#             'total_pages': self.page.paginator.num_pages,
#             'count': self.page.paginator.count,
#             'results': data
#         })


