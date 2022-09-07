from core.views import home
from django.urls import path
# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
]
# + static(settings.STATIC_URL,
#     document_root=settings.STATIC_ROOT)
