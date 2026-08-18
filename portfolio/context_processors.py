from django.conf import settings


def site_settings(request):
    """
    Makes global SEO and site settings
    available to all templates.
    """

    return {
        "SITE_NAME": settings.SITE_NAME,
        "SITE_DESCRIPTION": settings.SITE_DESCRIPTION,
        "SITE_KEYWORDS": settings.SITE_KEYWORDS,
        "SITE_AUTHOR": settings.SITE_AUTHOR,
    }