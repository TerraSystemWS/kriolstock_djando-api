from django.urls import path
from assets.views import DocumentoDetailView , DocumentoListView

from django.urls import path

urlpatterns = [
    path('documentos/', DocumentoListView.as_view()),
    path('documentos/<int:documento_id>/', DocumentoDetailView.as_view()),
]
