from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Review(models.Model):
    class PrivacyChoices(models.TextChoices):
        public = 'Public'
        private = 'Private'

    review_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey('library.Book', on_delete=models.CASCADE)
    review_text = models.TextField(max_length=450)
    visibility = models.CharField(
        max_length=7, 
        choices=PrivacyChoices.choices,
        default=PrivacyChoices.public
        )
    date_posted = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return "Review " + str(self.review_id)
