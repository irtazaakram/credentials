from django.contrib.staticfiles.storage import ManifestStaticFilesStorage


class CustomStaticFilesStorage(ManifestStaticFilesStorage):
    def hashed_name(self, name, content=None, filename=None):
        try:
            result = super().hashed_name(name, content, filename)
        except ValueError:
            result = name
        return result
