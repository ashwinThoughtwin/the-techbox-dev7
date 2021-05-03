from django.apps import AppConfig


class AppGadgetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_gadgets'

    def ready(self):
        import app_gadgets.signals
