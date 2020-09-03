from django.contrib import admin

from .models import Post, Category


class CategoryInLine(admin.TabularInline):
    model = Category.posts.through


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInLine,
    ]


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
