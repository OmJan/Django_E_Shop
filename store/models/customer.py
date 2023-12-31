from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=50)


    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return None

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False

    def __str__(self):
        return f"{self.first_name} {self.last_name}"