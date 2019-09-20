from django.conf import settings

from django_saml2_auth.plugins.metadata import MetadataPlugin


class DefaultMetadataHandler(MetadataPlugin):
    NAME = 'INLINE'

    @classmethod
    def get_metadata(cls):
        if 'METADATA_XML_STRING' in settings.SAML2_AUTH:
            return {
                'inline': [settings.SAML2_AUTH['METADATA_XML_STRING']]
            }