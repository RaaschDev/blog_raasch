from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path("",views.index, name="index"),
    path("posts/<int:post_id>",views.detail, name="post_detail"),
    path("ckeditor",include("ckeditor_uploader.urls")),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)