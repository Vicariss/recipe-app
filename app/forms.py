from django import forms
from .models import Recipe, Category

categories = Category.objects.all().values_list('name','name')



class RecipeModelForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #         super().__init__(*args, **kwargs)
    #         self.fields['category'].choices = [(obj.name, obj.name) for obj in Category.objects.all()]

    class Meta:
        model = Recipe
        fields = "__all__"

        widgets = {
            'category': forms.Select(choices=[(obj.name, obj.name) for obj in Category.objects.all()])
        }

    



   


