from django.db import models


class PromiseModel(models.Model):
    title = models.CharField( max_length=250)
    text = models.TextField()
    name = models.CharField(blank=True, max_length=50)
    color = models.CharField(blank=True, max_length=50)
    fontColor = models.CharField(blank=True, max_length=50)


    class Meta:
        verbose_name_plural = "Promises"

    def __str__(self):
        return self.title



