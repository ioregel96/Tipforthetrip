from django.contrib import admin
from .models import NewsPage, HistoryPage, HomePage

class PageContentAdmin(admin.ModelAdmin):
    pass
    # def has_add_permission(self, request):
    #     # Return False to disable add button
    #     return False
    
    # def has_delete_permission(self, request, obj=None):
    #     # Return False to disable delete button
    #     return False

admin.site.register(NewsPage, PageContentAdmin)
admin.site.register(HistoryPage, PageContentAdmin)
admin.site.register(HomePage, PageContentAdmin)
