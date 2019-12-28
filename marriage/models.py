from django.db import models

# Create your models here.

class Guest(models.Model):
    guest_name = models.CharField(max_length=50)
    guest_role = models.CharField(max_length=50, default="")
    message = models.CharField(max_length=500, default="")
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def replaceSpaces(self):
        url = 'https://marriage.my.id/tania-dika/' + str(self.id) + '/' + str(self.guest_name)
        return url.replace(' ', '%20')

    def __str__(self):
        url = self.replaceSpaces()
        return str(self.id) + ' ' + str(self.guest_name) + '. Link : ' + url