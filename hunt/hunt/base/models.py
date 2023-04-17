from django.db import models

# Create your models here.

class Clues(models.Model):
    clueid= models.CharField(max_length=20)
    clue = models.TextField()
    score = models.IntegerField()
    answer = models.TextField()



class Users(models.Model):
    userEmail = models.CharField(max_length=255, primary_key=True)
    userName = models.CharField(max_length=255)
    userPass = models.CharField(max_length=260)
    # scoreAndTime = models.IntegerField(null=True)
    totalScore = models.CharField(max_length=100,null=True)
    totalTime = models.CharField(max_length=100,null=True)
    attempts = models.IntegerField(null=True,default=-1)

    class Meta:
        get_latest_by = ['-totalScore']
        ordering = ['-totalScore']


class ScoreAndTime(models.Model):
    userEmail = models.CharField(max_length=255,primary_key=True)
    cl1Scr = models.IntegerField(null=True,default=0)
    cl1Tym = models.CharField(max_length=20,null=True)
    cl2Scr = models.IntegerField(null=True,default=0)
    cl2Tym = models.CharField(max_length=20,null=True)
    cl3Scr = models.IntegerField(null=True,default=0)
    cl3Tym = models.CharField(max_length=20,null=True)
    cl4Scr = models.IntegerField(null=True,default=0)
    cl4Tym = models.CharField(max_length=20,null=True)
    cl5Scr = models.IntegerField(null=True,default=0)
    cl5Tym = models.CharField(max_length=20,null=True)
    cl6Scr = models.IntegerField(null=True,default=0)
    cl6Tym = models.CharField(max_length=20,null=True)
    cl7Scr = models.IntegerField(null=True,default=0)
    cl7Tym = models.CharField(max_length=20,null=True)
    cl8Scr = models.IntegerField(null=True,default=0)
    cl8Tym = models.CharField(max_length=20,null=True)
    # cl9Scr = models.IntegerField(null=True,default=0)
    # cl9Tym = models.CharField(max_length=20,null=True)
    # cl0Scr = models.IntegerField(null=True,default=0)
    # cl0Tym = models.CharField(max_length=20,null=True)

    
