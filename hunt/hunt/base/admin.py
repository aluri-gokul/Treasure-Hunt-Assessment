from django.contrib import admin
from .models import Clues,Users,ScoreAndTime
 
@admin.register(Clues)
class RequestDemoAdmin(admin.ModelAdmin):    
  list_display = [field.name for field in Clues._meta.get_fields()]


@admin.register(Users)
class RequestDemoAdmin(admin.ModelAdmin):    
  list_display = ['userEmail','userName','userPass','totalScore','totalTime','attempts']

@admin.register(ScoreAndTime)
class RequestDemoAdmin(admin.ModelAdmin):    
  list_display = [field.name for field in ScoreAndTime._meta.get_fields()]

# Register your models here.


