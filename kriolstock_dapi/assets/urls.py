from django.urls import path
from assets.views import DocumentosView #, DocumentoCreateView

urlpatterns = [
    # path('docs/', DocumentosView.as_view(), name='listar_documentos'),
    # path('assets', DocumentosView.as_view),
    path('documentos/', DocumentosView.as_view(), name='documentos-list'),  # Para GET e POST
    # path('document-list/', DocumentosView.as_view()),
    # path('document-add/', DocumentoCreateView.as_view()),
]
