from django.contrib import admin
from .models import User, Contact

# Register your models here.
# @admin.register(User)
class ContactInline(admin.TabularInline):
    model = Contact.user_id.through
    list_display = ("street_address", "zip_code", "state")
    extra = 1

class UserAdmin(admin.ModelAdmin):
    # readonly_fields will allow non-editable fields to show up in the Admin portal
    readonly_fields = ("id","password", "user_role", "is_subscribed", "created_at", "updated_at", "last_login", "date_joined")
    inlines = [
        ContactInline
    ]

admin.site.register(User, UserAdmin)
admin.site.register(Contact)
