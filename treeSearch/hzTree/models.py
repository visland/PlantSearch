from django.db import models

class Months(models.Model):
    name = models.CharField(max_length=12)
    
    def __str__(self):        
        return self.name
        

class Tree(models.Model):
    # 基本信息
    zname = models.CharField(max_length=64, default=" ")
    kname = models.CharField(max_length=64, default=" ")
    sname = models.CharField(max_length=64, default=" ")
    ldname = models.CharField(max_length=64, default=" ")
    biename = models.CharField(max_length=64, default=" ")
    # 观赏特征
    morphology = models.CharField(max_length=300, default=" ")
    bloom_date = models.ManyToManyField(Months, blank=True,related_name="bloom_date")
    bloom_color = models.CharField(max_length=64, default=" ")
    fruit_date = models.ManyToManyField(Months, blank=True,related_name="fruit_date")
    fruit_color = models.CharField(max_length=64, default=" ")
    leaf_color = models.CharField(max_length=64, default=" ")

    def __str__(self):        
        return self.zname
    def bloom_month_list(self):
        return ','.join([i.name for i in self.bloom_date.all()])
    def fruit_month_list(self):
        return ','.join([i.name for i in self.fruit_date.all()])