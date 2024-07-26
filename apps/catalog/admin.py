from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Catalog

class CatalogAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)


admin.site.register(Catalog, CatalogAdmin)