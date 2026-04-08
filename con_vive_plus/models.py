from django.db import models

class House(models.Model):
    name = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default = 0)
    description = models.TextField(default = "")
    is_available = models.BooleanField(default = True)
    services = models.TextField(default = "")
    outside_image = models.ImageField(upload_to='houses/', null=True, blank=True)
    inside_image = models.ImageField(upload_to='houses/', null=True, blank=True)
    agent_name = models.CharField(max_length = 100, default = "")
    agent_phone = models.CharField(max_length = 20, default = "")
    agent_email = models.EmailField(default = "")

    def __str__(self):
        return f"{self.name} - {self.city}"
    
class Person(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    age = models.IntegerField()
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
    
class Expense(models.Model):
    title = models.CharField(max_length = 100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    paid_by = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.amount} EUROS "

class ContactMessage(models.Model):
    name = models.CharField(max_length = 100, default = "" )
    email =  models.EmailField(default = "")
    message = models.TextField(default = "")
    created_at = models.DateTimeField(auto_now_add = True)
          

