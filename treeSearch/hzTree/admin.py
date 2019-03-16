from django.contrib import admin
from hzTree.models import Tree, Months

class TreeAdmin(admin.ModelAdmin):
    list_display = ['species_name','family_name','genus_name', 'leaf_color', 'bloom_color','bloom_month_list', 'fruit_color','fruit_month_list']
admin.site.register(Tree,TreeAdmin)

class MonthsAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Months,MonthsAdmin)
