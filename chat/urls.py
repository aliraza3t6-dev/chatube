
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.accounts.urls')),
    path('chats/',include('apps.chats.urls')),
    path('global-chat/',include('apps.global_chat.urls'))
]
