from api.models import Record
from api.serializers import RecordSerializer
from django.db import transaction
from rest_framework.request import HttpRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class RecordAPIView(APIView):
    def get_queryset(self):
        return Record.objects.all()

    def get(self, request: HttpRequest, id: int = None) -> Response:
        try:
            queryset = self.get_queryset().filter(id=id) if id else self.get_queryset()
            serializer = RecordSerializer(instance=queryset, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                data={"error": f"Erro ao listar os Record: {str(error)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @transaction.atomic
    def post(self, request: HttpRequest) -> Response:
        try:
            serializer = RecordSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response(
                data={"error": f"Erro ao criar um Record: {str(error)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @transaction.atomic
    def delete(self, request: HttpRequest, id: int) -> Response:
        try:
            record = self.get_queryset().get(id=id)
            record.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(
                data={"error": f"Erro ao deletar um Record: {str(error)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @transaction.atomic
    def patch(self, request: HttpRequest, id: int) -> Response:
        try:
            record = self.get_queryset().get(id=id)
            serializer = RecordSerializer(instance=record, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                data={"error": f"Erro ao atualizar parcialmente um Record: {str(error)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )