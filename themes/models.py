from django.db import models


class Themes(models.Model):
    themes_title = models.CharField(max_length=255,verbose_name='Themes title')
    themes_txt = models.TextField(verbose_name='themes plan')

    def __str__(self):
        return F"{self.pk}.{self.themes_title}"

    class Meta:
        verbose_name = 'Themes'
        db_table = 'themes'
        verbose_name_plural = 'Themes'


