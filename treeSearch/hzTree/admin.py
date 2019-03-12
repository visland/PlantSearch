from django.contrib import admin
from hzTree.models import Tree, Months

class TreeAdmin(admin.ModelAdmin):
    list_display = ['zname','kname','sname','bloom_month_list','fruit_month_list']
admin.site.register(Tree,TreeAdmin)

class MonthsAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Months,MonthsAdmin)
