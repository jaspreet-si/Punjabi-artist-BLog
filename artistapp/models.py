from django.db import models

# Create your models here.
class artist(models.Model):
    Singer_name=models.CharField(max_length=100)
    Singer_img=models.ImageField(upload_to='images')
    singer_discription=models.TextField()
    

    def __str__(self):
        return self.Singer_name
class contact_us(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(unique=True)
    subject=models.CharField(max_length=200)
    Message=models.TextField()

    def __str__(self):
        return self.Name