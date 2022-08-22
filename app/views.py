from audioop import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Recipe
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.


class RecipeList(ListView):
    model = Recipe
    template_name = "app/recipe_list.html"
    context_object_name = "recipes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = context['recipes'].count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['recipes'] = context['recipes'].filter(Q(name__icontains=search_input) | Q(requirements__icontains=search_input))
            context['search_input'] = search_input
        return context


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




