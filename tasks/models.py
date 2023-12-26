from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)  

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)

class Subscription(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    payment_status = models.BooleanField(default=False)

class Task(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
