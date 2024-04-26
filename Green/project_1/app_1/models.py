from django.db import models

# Create your models here.
class Batsman(models.Model):
    name=models.CharField(max_length=100)
    matches=models.IntegerField()
    Runs=models.IntegerField()
    centuries=models.IntegerField()
    fifties=models.IntegerField()
    avg=models.FloatField()
    Highest_score=models.IntegerField()
    strike_rate=models.FloatField()
