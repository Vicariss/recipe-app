from django.urls import path
from .views import (
    RecipeList, 
    RecipeDetail, 
    RecipeUpdate, 
    RecipeDelete, 
    RecipeCreate, 
    LunchRecipeList,
    DinnerRecipeList,
    BreakfastRecipeList,
    )

urlpatterns = [
    path('', RecipeList.as_view(), name="recipes"),
    path('recipe/<int:pk>', RecipeDetail.as_view(), name="recipe"),
    path('recipe-update/<int:pk>', RecipeUpdate.as_view(), name="recipe-update"),
    path('recipe-delete/<int:pk>', RecipeDelete.as_view(), name="recipe-delete"),
    path('recipe-create/', RecipeCreate.as_view(), name="recipe-create"),
]