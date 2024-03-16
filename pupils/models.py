from django.db import models

class Pupil(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "pupils"

    def __str__(self):
        return self.name


class Grade(models.Model):
    pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    grade = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.subject} - {self.grade}"
