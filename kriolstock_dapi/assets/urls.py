from django.urls import path
from .views import DocumentosView

urlpatterns = [
    path('docs/', DocumentosView.as_view(), name='listar_documentos'),
]
