from django.apps import AppConfig


class StaticContentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pagecontent"
    verbose_name = "Page Content"
