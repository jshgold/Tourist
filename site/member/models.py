from django.db import models



class User(models.Model):
    userid = models.CharField(max_length=100, primary_key=True, verbose_name="UserID")
    email = models.EmailField(max_length=100, verbose_name="UserMail")
    password = models.CharField(max_length=100, verbose_name="UserPassword")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated")

    def __str__(self):
        return self.userid

    class Meta:
        db_table = "Members"
        verbose_name = "회원"
        verbose_name_plural = "회원"


