from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    subject = models.CharField(max_length=30, null=True, blank=True)  
    phone = models.CharField(max_length=12, null=True, blank=True)    
    problem = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Us"
