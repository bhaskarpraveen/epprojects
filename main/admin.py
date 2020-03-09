from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Detail
# Register your models here.
@admin.register(Detail)
class DetailAdmin(ImportExportModelAdmin):
    pass

