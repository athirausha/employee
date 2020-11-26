from django.db import models

# Create your models here.
class Login(models.Model):
    email = models.CharField(max_length=50, default='Nothing')
    password = models.CharField(max_length=50, default='Nothing')
    role = models.CharField(max_length=50, default='Nothing')
    class Meta:
        db_table = 'Login'

    def __int__(self):
        return self.id
class Employee(models.Model):
    name = models.CharField(max_length=50, default='Nothing')
    phone = models.BigIntegerField(default=0)
    email = models.CharField(max_length=50, default='Nothing')
    Address = models.CharField(max_length=50, default='Nothing')
    emp_image = models.FileField(blank=True, upload_to="media")
    gender    = models.CharField(max_length=50, default='Nothing')
    state    = models.CharField(max_length=50, default='Nothing')
    city    = models.CharField(max_length=50, default='Nothing')
    pincode    = models.CharField(max_length=50, default='Nothing')
    password    = models.CharField(max_length=50, default='Nothing')
    profile    = models.CharField(max_length=50, default='Nothing')
    log_fk=models.ForeignKey(Login,on_delete=models.CASCADE)

    class Meta:
        db_table = 'employee'

    def __int__(self):
        return self.id
   