from api.models import Record, RecordSerializer
from django.db import transaction
from rest_framework.request import HttpRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class RecordAPIView(APIView):
    def get_queryset(self):
        return Record.objects.all()

    def get(self, request: HttpRequest) -> Response:
        try:
            queryset = self.get_queryset()
            serializer = RecordSerializer(instance=queryset, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                data={"error": f"Erro ao listar os Records: {str(error)}"},
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
                data={"error": f"Erro ao criar um Registro: {str(error)}"},
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
                data={"error": f"Erro ao criar um Registro: {str(error)}"},
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
                data={"error": f"Erro ao criar um Registro: {str(error)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
