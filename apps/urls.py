from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from apps.views import IndexView,ProductUpdateView,DeleteProductView,AddUser

urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    path('del/<int:pk>',DeleteProductView.as_view(),name='delete_product'),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('add_user', AddUser.as_view(), name='add_user'),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)