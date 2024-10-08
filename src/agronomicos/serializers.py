""" Parsers for agronomicos app """
from rest_framework import serializers
from .models import UploadAgronomicosFilesModel


class UploadFileSerializer(serializers.ModelSerializer):
    """ Upload Settings """
    class Meta:
        """ Settings for model"""
        model = UploadAgronomicosFilesModel
        fields = '__all__'
