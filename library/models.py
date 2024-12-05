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
    

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=50)
    # profile_picture = models.ImageField(max_length=325)
    join_date = models.DateTimeField(auto_now_add=False)
    

    def __str__(self):
        return self.username


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