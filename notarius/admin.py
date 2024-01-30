from django.contrib import admin

from .models import Report, PurposeOfAssessment, ClientType





admin.site.site_header = "Приложение для формирование отчета"
admin.site.site_title = "Title админки"
admin.site.index_title = "Моя админка"

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('contractNumber', 'appraiser')
    search_fields = ('contractNumber',)
    list_editable = ("appraiser",)
    actions = ('make_zero',)
    def make_zero(self, request, queryset):
        queryset.update(contractNumber=0)

@admin.register(PurposeOfAssessment)
class PurposeOfAssessmentAdmin(admin.ModelAdmin):
    list_display = ('purposeOfAssessment1', )

@admin.register(ClientType)
class ClientTypeAdmin(admin.ModelAdmin):
    list_display = ('clientType', )




#admin.site.register(Report, ReportAdmin)