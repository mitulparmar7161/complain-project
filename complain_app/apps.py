from django.apps import AppConfig


class ComplainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'complain_app'

    def ready(self):
        import complain_app.signals