from django.db import models


class Numbers(models.Model):
    # This table will store all the numbers in our Plivo account.
    number = models.CharField(max_length=20, unique=True)
    active = models.BooleanField()
    region = models.CharField(max_length=50)
    created_on = models.DateTimeField()  # added_on field from Plivo API.
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number


class Messages(models.Model):
    # This will store all the messages received in our Plivo account.
    uuid = models.CharField(max_length=50, unique=True)
    message = models.CharField(max_length=480)
    # message_to = models.ForeignKey(Numbers)
    message_to = models.CharField(max_length=20)
    message_from = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message