from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('register/', user_views.register, name="register"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL,
#     document_root=settings.STATIC_ROOT)
