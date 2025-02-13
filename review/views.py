from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from review.models import Review
from .serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def user_reviews(request):

   if request.method == 'GET':
      reviews = Review.objects.filter(user_id=request.user)
      serializer = ReviewSerializer(reviews, many=True)
      return Response({'reviews': serializer.data})
   
   elif request.method == 'POST':
       serializer = ReviewSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def review_details(request, id):
        
    try:
        review = Review.objects.get(pk=id)
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
        return Response( {"message": "Review successfully deleted"}, status=status.HTTP_204_NO_CONTENT)

@api_view(["PATCH"])  
def update_visibility(id, visibility):
    review = get_object_or_404(Review, review_id=id)
   
    visibility_choices = ['Public', 'Private']
    if visibility not in visibility_choices:
        return Response({"detail": "Invalid visibility value."}, status=status.HTTP_400_BAD_REQUEST)
    
    review.visibility = visibility
    review.save()

    return Response({"message": "Visibility successfully updated"}, status = status.HTTP_200_OK)

@api_view(['GET'])
def book_reviews(request,id):
    reviews = Review.objects.filter(book_id=id)

    if not reviews.exists():
        return Response({'message': 'No reviews found for this book.'}, status=status.HTTP_404_NOT_FOUND)

    for review in reviews:
        return Response({'reviews': review.review_text})
    

@api_view(['GET'])
def book_review(request,book_id, review_id):
    try:
        review = Review.objects.get(book_id=book_id, review_id=review_id)
    except Review.DoesNotExist:
        return Response({'message': 'No such review found for this book.'}, status=status.HTTP_404_NOT_FOUND)

    return Response({'review': review.review_text})
    
    