from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    demo_feild = models.TextField(default='demo')
    email = models.EmailField()
    bio = models.TextField(null=True, blank=True)

    def get_author_name(self):
        return f'{self.name}'
    def __str__(self):
        return self.title
