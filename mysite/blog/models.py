from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    class Status(models.TextChoices):
        # Add status of a post such as draft, published
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"
    # Field for the post title. It translates into VARCHAR
    title = models.CharField(max_length=250)
    
    # Short label
    slug = models.SlugField(max_length=250)
    
    # Relationship betweeen users and posts
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blog_posts"
    )
    
    # Field for storing body of the post.
    body = models.TextField()
    
    # Publish date and time of the post. It will be translated
    # into a DATETIME column in the sql database
    publish = models.DateTimeField(default=timezone.now)
    
    # Store the date and time when the post was created.
    # Because of auto_now_add, the date will be saved automatically
    # when creating an object.
    created = models.DateTimeField(auto_now_add=True)
    
    # Store when the post was updated.
    updated = models.DateTimeField(auto_now=True)
    
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )
    
    class Meta:
        # This class defines metadata for the model.
        # Ordering is used to sort results by publish field.
        ordering = ["-publish"]
        # Define database indexes for the model
        indexes = [
            models.Index(fields=["-publish"]),
        ]
    
    # Default python method to return a string with human-readable
    # representation of the object. It will be used for displaying 
    # the name of the object in places, such as, django admin site
    def __str__(self):
        return self.title
