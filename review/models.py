from django.db import models
from user.models import User
from library.models import Book

# Create your models here.

class Review(models.Model):
    class PrivacyChoices(models.TextChoices):
        public = 'Public'
        private = 'Private'

    review_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_text = models.TextField(max_length=450)
    is_public = models.CharField(
        max_length=7, 
        choices=PrivacyChoices.choices,
        default=PrivacyChoices.public
        )
    date_posted = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return "Review " + self.review_id
