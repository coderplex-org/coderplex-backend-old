from django.db import models

# Create your models here.


class CurriculumBook(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField()
    image = models.ImageField(default=None, null=True, blank=True)
    description = models.TextField()
    
    created_by = models.ForeignKey('auth.User')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey('auth.User', related_name="updated_books")
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


class CurriculumPage(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField()
    content = models.TextField()
    
    created_by = models.ForeignKey('auth.User')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey('auth.User', related_name="updated_pages")
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title