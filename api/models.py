from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name[:20]