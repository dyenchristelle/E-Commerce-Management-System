from django.db import models

# Create your models here.
class AdminLogin(models.Model):
    username = models.CharField(max_length=250, db_column="admin_username", unique=True)
    password = models.CharField(max_length=250, db_column="password")

    class Meta:
        db_table = "AdminLogin"

    def __str__(self):
        return self.username
    

class Products(models.Model):
    pr_name = models.CharField(max_length=250)
    pr_quantity = models.IntegerField()
    pr_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "products_furniture"
