from django.contrib import admin
from .models import Ekologiya, Category, Menyu, Katalog, News



class EkoAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content',)
    list_editable = ('is_published',)
    list_filter = ('is_published','category')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

class MenyuAdmin(admin.ModelAdmin):
        list_display = ('title',)
        list_display_links = ('title',)
        search_fields = ('title',)


class KatalogAdmin(admin.ModelAdmin):
    list_display = ('okpo','soato', 'name','biznes')
    list_display_links = ('okpo',)
    search_fields = ('okpo', 'name',)
    list_editable = ('biznes',)
    list_select_related = True

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'content', 'is_published',)
    search_fields = ('title', 'content',)
    list_select_related = True
    list_editable = ('is_published', 'category',)
    list_filter = ('is_published', 'category')

admin.site.register(Ekologiya, EkoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Menyu, MenyuAdmin)
admin.site.register(Katalog, KatalogAdmin)
admin.site.register(News, NewsAdmin)


