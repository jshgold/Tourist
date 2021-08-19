from django.db import models


class Content(models.Model):
    spot = models.CharField(max_length=100,primary_key=True,verbose_name="Tourspot")
    cont = models.TextField(verbose_name="content")
    tourimg = models.CharField(max_length=100,verbose_name="image")
    dep = models.CharField(max_length=100,verbose_name="place")
    yea = models.IntegerField(null=True,verbose_name="year")
    mont = models.IntegerField(null=True,verbose_name="month")


    def __str__(self):
        return self.spot

    class Meta:
        db_table="Datas"
        verbose_name="여행지"
        verbose_name_plural="여행지들"

