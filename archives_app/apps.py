from django.apps import AppConfig
from django.conf import settings
import os

class ArchivesAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'archives_app'

    def ready(self):
        # 在应用准备好时确保MEDIA_ROOT目录存在
        media_root = settings.MEDIA_ROOT
        if not os.path.exists(media_root):
            os.makedirs(media_root)
