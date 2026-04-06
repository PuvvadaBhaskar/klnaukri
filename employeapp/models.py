from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    employee_id = models.CharField( max_length=100,primary_key=True)
    employee_name = models.CharField( max_length=100)
    employee_location = models.CharField(max_length=100)
    empoyee_phone = models.CharField( max_length=100)
    employee_email = models.CharField(max_length=100)

    def __str__(self):
        return self.employee_name