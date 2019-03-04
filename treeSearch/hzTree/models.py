from django.db import models

# Create your models here.
class Tree(models.Model):
    zname = models.CharField(max_length=64)
    kname = models.CharField(max_length=64)
    
    class Meta:
        managed = True
        # db_table = 'Trees'

    def __str__(self):        
        return self.zname

CONDITION_CHOICES = (
    ('zname', '中文名'),
    ('kname', '科名'),
)

class QueryUser(models.Model):
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    queryContent = models.CharField(max_length=100)

    def __str__(self):        
        return self.condition