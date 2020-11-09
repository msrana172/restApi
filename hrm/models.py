from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

class Users(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    ranking = models.FloatField()
    
    def upload_photo(self, filename):
        path = 'hrm/photo/{}'.format(filename)
    photo = models.ImageField(upload_to =upload_photo, null = True, blank = True)  

    def upload_file(self, filename):
        path = 'hrm/file/{}'.format(filename)
    resume = models.FileField(upload_to=upload_file, null=True, blank=True)    

    def __str__(self):
        return f"{self.employee_id} - {self.name}"