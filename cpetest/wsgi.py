"""
WSGI config for cpetest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cpetest.settings')

application = get_wsgi_application()
# import os
# from django.core.wsgi import get_wsgi_application
# from dj_static import Cling # <- 加入
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# application = Cling(get_wsgi_application()) # <- 修改