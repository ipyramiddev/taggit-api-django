try:
    import django
except ImportError:
    # setup.py and docs do not have Django installed.
    django = None

VERSION = (2, 1, 0)
__version__ = ".".join(str(i) for i in VERSION)

if django and django.VERSION < (3, 2):
    default_app_config = "taggit.apps.TaggitAppConfig"
