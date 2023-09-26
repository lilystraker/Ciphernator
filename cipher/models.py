from django.db import models


class SDES(models.Model):
  plaintext = models.CharField(max_length=8)