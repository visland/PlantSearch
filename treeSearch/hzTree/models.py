from django.db import models

# Create your models here.
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
    
    class Meta:
        managed = True
        # db_table = 'Trees'

    def __str__(self):        
        return self.zname

CONDITION_CHOICES = (
    # 基本信息
    ('zname', '中文名'),
    ('ldname', '拉丁名'),
    ('kname', '科名'),
    ('sname', '属名'),
    ('biename', '别名'),
    # 观赏特征
    ('morphology', '形态'),
    ('bloom_date', '花期'),
    ('bloom_color', '花色'),
    ('fruit_date', '果期'),
    ('fruit_color', '果色'),
    ('leaf_color', '叶色'),
)

class QueryUser(models.Model):
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    queryContent = models.CharField(max_length=100)
    queryContent2 = models.CharField(max_length=100)

    def __str__(self):        
        return self.condition