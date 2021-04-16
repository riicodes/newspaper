from django.contrib import admin
from .models import Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    readonly_fields = ('date',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
