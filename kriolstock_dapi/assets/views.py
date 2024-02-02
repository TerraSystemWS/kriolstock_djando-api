from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Documento
from .serializers import DocumentoSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated

permission_classes = [IsAuthenticated]

class DocumentosView(APIView):
    def get(self, request):
        print(request.user)
        documentos = Documento.objects.all()
        serializer = DocumentoSerializer(documentos, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        
        # if not request.user.is_authenticated:
        #     return Response({"message": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = DocumentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request):
    #     # Verifica se o usuário está autenticado
    #     if not request.user.is_authenticated:
    #         raise AuthenticationFailed('Autenticação necessária')

    #     # Serializa os dados do documento recebidos na requisição
    #     serializer = DocumentoSerializer(data=request.data)

    #     # Valida os dados do documento
    #     if serializer.is_valid():
    #         # Salva o documento no banco de dados associado ao usuário autenticado
    #         serializer.save(user=request.user)
    #         # Retorna os dados do documento criado com o status 201 Created
    #         return Response(serializer.data, status=201)
    #     # Retorna erros de validação caso os dados do documento sejam inválidos
    #     return Response(serializer.errors, status=400)