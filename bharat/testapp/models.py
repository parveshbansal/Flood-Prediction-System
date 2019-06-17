from django.db import models
class User(models.Model):
	name=models.CharField(max_length=30)
	phoneno=models.IntegerField()
	status_choices=((1,'hissar'),(2,'rohtak'),(3,'maham'))
	village=models.IntegerField(choices=status_choices,default='hissar')
