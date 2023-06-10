from django.db import transaction
from rest_framework import status
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Image
from api.serializers import ImageSerializer


class ImageAPIView(APIView):
    def get_queryset(self):
        return Image.objects.all()

    def get(self, request: HttpRequest, id: int = None) -> Response:
        try:
            queryset = self.get_queryset().filter(id=id) if id else self.get_queryset()
            serializer = ImageSerializer(instance=queryset, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                data={"error": f"Erro ao listar Image: {str(error)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @transaction.atomic
    def post(self, request: HttpRequest) -> Response:
        try:
            serializer = ImageSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response(
                data={"error": f"Erro ao criar um Image: {str(error)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @transaction.atomic
    def delete(self, request: HttpRequest, id: int) -> Response:
        try:
            image = self.get_queryset().get(id=id)
            image.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(
                data={"error": f"Erro ao deletar um Image: {str(error)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @transaction.atomic
    def patch(self, request: HttpRequest, id: int) -> Response:
        try:
            image = self.get_queryset().get(id=id)
            serializer = ImageSerializer(
                instance=image, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                data={"error": f"Erro ao atualizar parcialmente um Image: {str(error)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
