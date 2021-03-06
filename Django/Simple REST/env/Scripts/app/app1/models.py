from django.db import models
import uuid

class Computer ( models . Model ):
    id = models . UUIDField ( primary_key = True , default = uuid . uuid4 , editable = False )
    manufacturer = models . CharField (max_length =200)
    modelName = models . CharField ( max_length =200)
    releaseDate = models . DateTimeField (blank = True , null = True )
# Create your models here.
