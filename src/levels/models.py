""" DB """
from django.db import models

# Create your models here.


class LevelsModel(models.Model):
    """ DB Levels """
    field_one = models.CharField(max_length=100)
    field_two = models.CharField(max_length=100)
    field_three = models.CharField(max_length=100)
    field_four = models.CharField(max_length=100)
    field_five = models.CharField(max_length=100)
    field_six = models.CharField(max_length=100)
    field_seven = models.CharField(max_length=100)
    field_eight = models.CharField(max_length=100)
    field_nine = models.CharField(max_length=100)
    field_ten = models.CharField(max_length=100)

    # * Additional fields
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    db_table = 'levels'
    verbose_name = 'level'
    verbose_name_plural = 'levels'


class LevelsUploadFilesModel(models.Model):
    """ Upload File """
    file = models.FileField(upload_to="address")

    # * Auditoría
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        """ Settings for model """
        db_table = 'uploads_levels'
        verbose_name = 'upload levels'
        verbose_name_plural = 'upload levels'

    def __str__(self) -> str:
        """ String representation """
        return f"{self.file.name}"
