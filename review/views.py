from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from review.models import Review
from .serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def user_reviews(request):

   if request.method == 'GET':
      serializer = ReviewSerializer()
      return Response({'review': serializer.data})
   elif request.method == 'POST':
       serializer = ReviewSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_200_OK)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def review_details(request, id):
        
    try:
        review = Review.objects.first(pk=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    
    if request.method == 'GET':
        username = review.user_id.username
        book = review.book_id.book_title
        serializer = ReviewSerializer(review)
        return Response({'review': serializer.data, 'username':username, 'book': book})
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        review.delete()
        return Response( {"message": "Book successfully deleted"}, status=status.HTTP_204_NO_CONTENT)