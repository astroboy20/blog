from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Blog(models.Model):

    STATUS_OPTIONS = (
        ('DRAFT', 'draft'),
        ('PUBLISHED', 'published'),
        ('TRASHED', 'trash'),
    )

    title = models.CharField(max_length=104, unique=True)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_OPTIONS,
                              max_length=10, default='DRAFT')
    body = models.TextField()
    banner = models.ImageField(upload_to='blog/banner/', blank=True)

    def __str__(self) -> str:
        return f"{self.title} by {self.author.username}"

    def get_queryset(self):
        return super().get_queryset().filter(status='PUBLISHED')
