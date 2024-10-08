""" DB """
from django.db import models
from src.levels.models import LevelsModel

# Create your models here.


class UploadAgronomicosFilesModel(models.Model):
    """ Upload File """
    levels = models.ForeignKey(LevelsModel, on_delete=models.CASCADE)
    file = models.FileField(upload_to="agronomicos")
    nombre_archivo = models.CharField(max_length=255, blank=True, null=True)

    # * Auditoría
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        """ Settings for model """
        db_table = 'upload agronomicos'
        verbose_name = 'upload agronomico'
        verbose_name_plural = 'upload agronomicos'

    def __str__(self) -> str:
        """ String representation """
        return f"{self.file.name}"
