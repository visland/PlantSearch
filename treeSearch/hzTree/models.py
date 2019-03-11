from django.db import models

class Tree(models.Model):
    # 基本信息
    zname = models.CharField(max_length=64, default=" ")
    kname = models.CharField(max_length=64, default=" ")
    sname = models.CharField(max_length=64, default=" ")
    ldname = models.CharField(max_length=64, default=" ")
    biename = models.CharField(max_length=64, default=" ")
    # 观赏特征
    morphology = models.CharField(max_length=300, default=" ")
    bloom_date = models.CharField(max_length=64, default=" ")
    bloom_color = models.CharField(max_length=64, default=" ")
    fruit_date = models.CharField(max_length=64, default=" ")
    fruit_color = models.CharField(max_length=64, default=" ")
    leaf_color = models.CharField(max_length=64, default=" ")

    def __str__(self):        
        return self.zname