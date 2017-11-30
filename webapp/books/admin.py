from django.contrib import admin
from . import models
# Register your models here.


class GenericAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Book, GenericAdmin)
admin.site.register(models.Chapter, GenericAdmin)
admin.site.register(models.Page, GenericAdmin)
# admin.site.register(models.ChapterPageRelationShip)
# admin.site.register(models.BookChapterRelationShip)
