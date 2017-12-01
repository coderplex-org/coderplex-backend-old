from django.db import models

# Create your models here.


class Book(models.Model):
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


class Chapter(models.Model):
    title = models.CharField(max_length=25, db_index=True)
    slug = models.SlugField()
    content = models.TextField()
    book = models.ForeignKey(Book, default=None, null=True)
    position = models.PositiveIntegerField(default=None, null=True)

    created_by = models.ForeignKey('auth.User')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey('auth.User', related_name="updated_chapter")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0}-{1}".format(self.title, self.book)


class Page(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField()
    content = models.TextField()
    chapter = models.ForeignKey(Chapter, default=None, null=True)
    position = models.PositiveIntegerField(default=None, null=True)

    created_by = models.ForeignKey('auth.User')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey('auth.User', related_name="updated_pages")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
