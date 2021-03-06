from django.db import models


class React(models.Model):
    name = models.CharField(verbose_name="Название", max_length=30)
    qual = models.CharField(verbose_name="Квалификация", max_length=20, null=True)
    date = models.DateField(verbose_name="Дата поступления")
    prov = models.CharField(verbose_name="Поставщик", max_length=20, blank=True, null=True)
    srok = models.DateField(verbose_name="Срок годности", null=True, blank=True)
    place = models.CharField(verbose_name="Место хранения", max_length=30, null=True, blank=True)
    mass = models.FloatField(verbose_name="Масса, кг", null=True, blank=True)

    def add(self):
        self.save()

    def __str__(self):
        return self.name
