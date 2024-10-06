""" Views """
import polars as pl
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from .models import AddressModel
from .serializers import AddressSerializer, UploadFileSerializer


class UpladExcelView(APIView):
    """ Upload Excel File """
    allowed_methods = ['GET', 'POST']
    parser_classes = [MultiPartParser]

    def get(self, request, parroquia_name: None):
        """ List Addresses """
        if parroquia_name:
            try:
                parroquias = AddressModel.objects.get(parroquia=parroquia_name)
                serializer = AddressSerializer(parroquias)
                return Response(
                  {
                    'status': 200,
                    'data': serializer.data
                  },
                  status=status.HTTP_200_OK
                )
            except AddressModel.DoesNotExist:
                return Response(
                  {
                    'status': 404,
                    'data': "Parroquia Not found"
                  }, status=status.HTTP_404_NOT_FOUND
                )

    def post(self, request, *args, **kwargs):
        """ Upload File """
        serializer = UploadFileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        excel_file = serializer.save()
        file_path = excel_file.file.path

        # * DF Polars
        df = pl.read_excel(file_path, engine="openpyxl")
        df.drop_nulls()
        df.unique()

        # * Llenando la DB
        for record in df.rows(named=True):
            AddressModel.objects.create(
                provincia=record['Provincia'],
                canton=record['Canton'],
                parroquia=record['Parroquia']
            )

        return Response(
            {
                "message": "File Upload and Data Saved"
            }, status=status.HTTP_201_CREATED
        )
