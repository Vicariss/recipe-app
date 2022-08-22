from ast import Del, Delete
from audioop import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Recipe
from django.urls import reverse_lazy

# Create your views here.


class RecipeList(ListView):
    model = Recipe
    template_name = "app/recipe_list.html"
    context_object_name = "recipes"


class RecipeDetail(DetailView):
    model = Recipe
    context_object_name = "recipe"


class RecipeCreate(CreateView):
    model = Recipe
    success_url = reverse_lazy("recipes")
    fields = '__all__'
    template_name = "app/recipe_create.html"


class RecipeUpdate(UpdateView):
    model = Recipe
    fields = '__all__'
    success_url = reverse_lazy('recipes')
    template_name = "app/recipe_update.html"


class RecipeDelete(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes')
    template_name = "app/recipe_delete.html"




