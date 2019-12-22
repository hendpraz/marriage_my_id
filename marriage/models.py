from django.db import models

# Create your models here.

class Guest(models.Model):
    guest_name = models.CharField(max_length=50)
    guest_role = models.CharField(max_length=50, default="")
    message = models.CharField(max_length=500, default="")
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.guest_name) + ': ' + str(self.message) 