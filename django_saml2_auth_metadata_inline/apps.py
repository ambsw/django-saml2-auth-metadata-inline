from django import apps


class AppConfig(apps.AppConfig):
    name = 'django_saml2_auth_metadata_inline'

    def ready(self):
        # import plugins
        # noinspection PyUnresolvedReferences
        from . import plugins
