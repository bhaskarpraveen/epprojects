from django.db import models

# Create your models here.
class Detail(models.Model):
  #  team_name = models.CharField(max_length=50)
    project_id = models.CharField(max_length=2)
    member1=models.CharField(max_length=9)
    member2=models.CharField(max_length=9)
    member3=models.CharField(max_length=9)
    member4=models.CharField(max_length=9)
    member5=models.CharField(max_length=9)


    def __str__(self):
        return "Team"+str(self.id)
