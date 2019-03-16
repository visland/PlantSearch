from django.db import models

class Months(models.Model):
    name = models.CharField(max_length=12)
    
    def __str__(self):        
        return self.name
        
TREE_TYPE_CHOICES = (
    ('常绿乔木','常绿乔木'),
    ('落叶乔木','落叶乔木'),
)

class Tree(models.Model):
    # 基本信息
    species_name = models.CharField(max_length=16, default=" ")
    family_name = models.CharField(max_length=16, default=" ")
    genus_name = models.CharField(max_length=16, default=" ")
    latin_name = models.CharField(max_length=64, default=" ")
    alternative_name = models.CharField(max_length=64, default=" ")
    #类型信息
    tree_type = models.CharField(max_length=16, choices=TREE_TYPE_CHOICES, default="")
    tree_value = models.CharField(max_length=64, default=" ")
    tree_shape = models.CharField(max_length=64, default=" ")
    # 观赏特征
    morphology = models.CharField(max_length=300, default=" ")

    bloom_date = models.ManyToManyField(Months, blank=True,related_name="bloom_date")
    bloom_color = models.CharField(max_length=64, default=" ")
    bloom_color_spring = models.CharField(max_length=64, default="无")
    bloom_color_summer = models.CharField(max_length=64, default="无")
    bloom_color_autumn = models.CharField(max_length=64, default="无")
    bloom_color_winter = models.CharField(max_length=64, default="无")

    fruit_date = models.ManyToManyField(Months, blank=True,related_name="fruit_date")
    fruit_color = models.CharField(max_length=64, default=" ")
    fruit_color_spring = models.CharField(max_length=64, default="无")
    fruit_color_summer = models.CharField(max_length=64, default="无")
    fruit_color_autumn = models.CharField(max_length=64, default="无")
    fruit_color_winter = models.CharField(max_length=64, default="无")

    leaf_color = models.CharField(max_length=64, default=" ")
    leaf_color_spring = models.CharField(max_length=64, default="无")
    leaf_color_summer = models.CharField(max_length=64, default="无")
    leaf_color_autumn = models.CharField(max_length=64, default="无")
    leaf_color_winter = models.CharField(max_length=64, default="无")
    # 生态习性
    geo_distribution = models.CharField(max_length=300, default=" ")
    propensity = models.CharField(max_length=300, default=" ")
    soil = models.CharField(max_length=300, default=" ")
    pollution_tolerance = models.CharField(max_length=300, default=" ")


    def __str__(self):        
        return self.species_name
    def bloom_month_list(self):
        return ','.join([i.name for i in self.bloom_date.all()])
    def fruit_month_list(self):
        return ','.join([i.name for i in self.fruit_date.all()])