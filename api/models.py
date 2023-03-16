from django.db import models

# Create your models here.
# Models documentation
# https://docs.djangoproject.com/en/4.1/topics/db/models/

# ID fields are added automatically by models, so we won't need to worry about adding them manually
# All model fields are required by default, you have to specify blank=True in order for a field to be nullable
# class Product(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField(max_length=1000)
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     flavor_profile = models.CharField(max_length=25)

#class Contact(models.Model):
    # user = models.ForeignKey(User)
#    street_address = models.TextField(max_length=100)
#    zip_code = models.CharField(max_length=15)
#    state = models.CharField(max_length=15)
#    phone_number = models.CharField(max_length=15)

class Order(models.Model):
    # user = models.ForeignKey(User)
    order_status = models.CharField(max_length=50)
    date_ordered = models.DateField()


###################### Junction Tables ######################

class ProductOrder(models.Model):
    # product = models.ForeignKey(Product)
    # order = models.ForeignKey(Order)
    quantity = models.IntegerField()



# class UserContact(models.Model):
    # user = models.ForeignKey(User)
    # contact = models.ForeignKey(Contact)
