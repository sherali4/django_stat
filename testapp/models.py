from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

class Rubric(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    def get_absolute_url(self):
        return reverse('rubric', kwargs={"pk":self.pk})
    def __str__(self):
        return self.name
    class MPTTMeta:
        order_insertion_by = ['name']

class Articlesa(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Rubric, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
