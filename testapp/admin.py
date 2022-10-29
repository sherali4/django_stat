from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin, TreeRelatedFieldListFilter
from .models import Rubric, Articlesa

admin.site.register(Rubric, MPTTModelAdmin)
admin.site.register(Articlesa)


class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_indent_field = "some_node_field"

class MyDraggableMPTTAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 50

class MyTreeRelatedFieldListFilter(TreeRelatedFieldListFilter):
    mptt_level_indent = 20