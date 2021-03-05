from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices

# Create your models here.
class Item(models.Model) :
    status_choices = [ ('C' , "Completed") , ('P' , "Pending") ] 
    priority_choices = [ (1 , '1️⃣' ) ,  (2 , '2️⃣'), (3 , '3️⃣'), 
            (4 , '4️⃣'), (5 , '5️⃣') 
    ]

    user = models.ForeignKey( to = User , on_delete= models.CASCADE)
    title = models.CharField(max_length= 50 )
    status = models.CharField(max_length= 2 , choices= status_choices , default= 'P') 
    priority = models.IntegerField(choices= priority_choices , default = 1 )


    def __str__(self) :
        return self.title  
