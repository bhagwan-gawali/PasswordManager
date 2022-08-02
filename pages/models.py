from django.db import models
from accounts.models import CustomUser

class GeneralPassword(models.Model):
    title = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    category = models.CharField(max_length=10)
    notes = models.TextField()
    delete_pass = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class CardData(models.Model):
    cc_number = models.CharField(verbose_name='Card Number', max_length=16)
    cc_holder_name = models.CharField(verbose_name='Card Holder Name', max_length=200)
    exp_date = models.CharField(verbose_name='Expiry Date', max_length=200)
    ccv_code = models.CharField(verbose_name='CCV/Security Code', max_length=3)
    cc_notes = models.TextField()
    delete_card = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.cc_holder_name
