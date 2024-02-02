from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from .models import Documento
from .serializers import DocumentoSerializer

class DocumentoDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_documento(self, documento_id):
        try:
            return Documento.objects.get(id=documento_id, user=self.request.user)
        except Documento.DoesNotExist:
            raise NotFound("Documento not found")

    def get(self, request, documento_id):
        documento = self.get_documento(documento_id)
        serializer = DocumentoSerializer(documento)
        return Response(serializer.data)

    def post(self, request):
        serializer = DocumentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, documento_id):
        documento = self.get_documento(documento_id)
        serializer = DocumentoSerializer(documento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, documento_id):
        documento = self.get_documento(documento_id)
        documento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DocumentoListView(APIView):
    permission_classes = [IsAuthenticated]

    def get_all_documentos(self):
        return Documento.objects.filter(user=self.request.user)

    def get(self, request):
        documentos = self.get_all_documentos()
        serializer = DocumentoSerializer(documentos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DocumentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
