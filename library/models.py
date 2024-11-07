from django.db import models

class Library(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=225)
    book_author = models.CharField(max_length=225)
    book_summary = models.TextField(max_length=325)
    

    def __str__(self):
        return self.book_title

# class Summary(models.Model):
#     library = models.OneToOneField(Library, on_delete=models.CASCADE) # Establish a OneToOne relationship with Library
#     book_summary = models.TextField()

#     def __str__(self):
#         return f"Summary of {self.library.book_title}"
