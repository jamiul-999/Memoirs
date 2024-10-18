from django.db import models

# Create your models here.

class Post(models.Model):
    # Field for the post title. It translates into VARCHAR
    title = models.Charfield(max_length = 250)
    # Short label
    slug = models.SlugField(max_length = 250)
    # Field for storing body of the post.
    body = models.TextField()

# Default python method to return a string with human-readable
# representation of the object. It will be used for displaying 
# the name of the object in places, such as, django admin site
def __str__(self):
    return self.title
