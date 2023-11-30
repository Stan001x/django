from django.contrib import admin

from .models import Report





admin.site.site_header = "Приложение для формирование отчета"
admin.site.site_title = "Title админки"
admin.site.index_title = "Моя админка"

class ReportAdmin(admin.ModelAdmin):
    list_display = ('clientname', 'contractNumber', 'appraiser')
    search_fields = ('clientname',)
    list_editable = ("contractNumber",)
    actions = ('make_zero',)
    def make_zero(self, request, queryset):
        queryset.update(contractNumber=0)

admin.site.register(Report, ReportAdmin)