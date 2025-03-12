from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Book(models.Model):
    book_id = models.AutoField(primary_key=True )
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=225)
    book_author = models.CharField(max_length=225)
    genre = models.CharField(max_length=50)
    book_summary = models.TextField(max_length=325)
    book_content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    

    def __str__(self):
        return self.book_title
    
