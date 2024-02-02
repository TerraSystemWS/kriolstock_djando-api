from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from assets.models import Documento
from assets.serializers import DocumentoSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class DocumentosView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]  # Permite acesso público à rota GET e autenticação para a rota POST

    def get(self, request):
        documentos = Documento.objects.all()
        serializer = DocumentoSerializer(documentos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"message": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = DocumentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
