from django.db import models

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=225)
    book_author = models.CharField(max_length=225)
    genre = models.CharField(max_length=50)
    book_summary = models.TextField(max_length=325)
    book_content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.book_title
    
