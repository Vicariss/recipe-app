from django import forms
from .models import Recipe, Category

categories = Category.objects.all().values_list('name','name')



class RecipeModelForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = "__all__"

        widgets = {
            'category': forms.Select(choices=[(obj.name, obj.name) for obj in Category.objects.all()])
        }

