from django.contrib import admin
from .models import Post

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display= ['title', 'subtitle', 'author', 'publish', 'status']
    list_filter= ['status', 'author']
    search_fields=['title', 'author', 'body']
    prepopulated_fields={'subtitle':('title',)}
    raw_id_fields=['author']
    date_hierarchy='publish'
    ordering=['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS
    

# Register your models here.
