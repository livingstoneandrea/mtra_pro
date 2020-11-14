"""
ASGI config for mtra_pro project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import django

from django.core.asgi import get_asgi_application
from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mtra_pro.settings')

#application = get_asgi_application()

django.setup()
application = get_default_application()

# application = ProtocolTypeRouter({
#     # Django's ASGI application to handle traditional HTTP requests
#     "http": get_asgi_application()

#     # WebSocket chat handler
#     "websocket": AuthMiddlewareStack(
#         URLRouter([
#             url(r"^chat/admin/$", AdminChatConsumer.as_asgi()),
#             url(r"^chat/$", PublicChatConsumer.as_asgi()),
#         ])
#     ),
# })