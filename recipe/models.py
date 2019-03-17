from django.db import models


class IngredientType(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    source = models.CharField(max_length=200, blank=False)
    cookTime = models.CharField(max_length=200, blank=True)
    instructions = models.TextField()
    ingredient1 = models.CharField(max_length=200)
    ingredient1_type = models.ForeignKey(IngredientType, on_delete=models.CASCADE, related_name='ingredient1_type')

    ingredient2 = models.CharField(max_length=200, blank=True)
    ingredient2_type = models.ForeignKey(IngredientType, on_delete=models.CASCADE, related_name='ingredient2_type', blank=True, null=True)

    ingredient3 = models.CharField(max_length=200, blank=True)
    ingredient3_type = models.ForeignKey(IngredientType, on_delete=models.CASCADE, related_name='ingredient3_type', blank=True, null=True)

    ingredient4 = models.CharField(max_length=200, blank=True)
    ingredient4_type = models.ForeignKey(IngredientType, on_delete=models.CASCADE, related_name='ingredient4_type', blank=True, null=True)

    ingredient5 = models.CharField(max_length=200, blank=True)
    ingredient5_type = models.ForeignKey(IngredientType, on_delete=models.CASCADE, related_name='ingredient5_type', blank=True, null=True)

    ingredient6 = models.CharField(max_length=200, blank=True)
    ingredient6_type = models.ForeignKey(IngredientType, on_delete=models.CASCADE, related_name='ingredient6_type', blank=True, null=True)


    ingredient7_type = models.ForeignKey(IngredientType, on_delete=models.CASCADE, related_name='ingredient7_type', blank=True, null=True)
    ingredient7 = models.CharField(max_length=200, blank=True)

    ingredient8_type = models.ForeignKey(IngredientType, on_delete=models.CASCADE, related_name='ingredient8_type', blank=True, null=True)
    ingredient8 = models.CharField(max_length=200, blank=True)

    ingredient9_type = models.ForeignKey(IngredientType, on_delete=models.CASCADE, related_name='ingredient9_type', blank=True, null=True)
    ingredient9 = models.CharField(max_length=200, blank=True)

    ingredient10_type = models.ForeignKey(IngredientType, on_delete=models.CASCADE, related_name='ingredient10_type', blank=True, null=True)
    ingredient10 = models.CharField(max_length=200, blank=True)

    ingredient11_type = models.ForeignKey(IngredientType, on_delete=models.CASCADE, related_name='ingredient11_type', blank=True, null=True)
    ingredient11 = models.CharField(max_length=200, blank=True)

    ingredient12_type = models.ForeignKey(IngredientType, on_delete=models.CASCADE, related_name='ingredient12_type', blank=True, null=True)
    ingredient12 = models.CharField(max_length=200, blank=True)

    ingredient13_type = models.ForeignKey(IngredientType, on_delete=models.CASCADE, related_name='ingredient13_type', blank=True, null=True)
    ingredient13 = models.CharField(max_length=200, blank=True)

    ingredient14_type = models.ForeignKey(IngredientType, on_delete=models.CASCADE, related_name='ingredient14_type', blank=True, null=True)
    ingredient14 = models.CharField(max_length=200, blank=True)

    ingredient15_type = models.ForeignKey(IngredientType, on_delete=models.CASCADE, related_name='ingredient15_type', blank=True, null=True)
    ingredient15 = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
