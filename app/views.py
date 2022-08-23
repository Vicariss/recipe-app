from audioop import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Recipe, Category
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import RecipeModelForm

# Create your views here.


class RecipeList(ListView):
    model = Recipe
    template_name = "app/recipe_list.html"
    context_object_name = "recipes"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = context['recipes'].count()

        context['categories'] = Category.objects.all()

        search_input = self.request.GET.get('search-area') or ''
        choose_category = self.request.GET.get('choose-category')
        if choose_category:
            context["recipes"] = context['recipes'].filter(category__icontains=choose_category)
            context['chosen_category'] = choose_category
        if search_input:
            context['recipes'] = context['recipes'].filter(
                Q(name__icontains=search_input) | Q(requirements__icontains=search_input))[:2]
                # https://docs.djangoproject.com/en/4.1/topics/db/queries/#lookups-that-span-relationships
            context['search_input'] = search_input
        return context





class LunchRecipeList(ListView):
    model = Recipe
    context_object_name = "recipes"
    template_name = "app/recipe_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = context['recipes'].filter(category__icontains="Lunch")
        return context


class DinnerRecipeList(ListView):
    model = Recipe
    context_object_name = "recipes"
    template_name = "app/recipe_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = context['recipes'].filter(category__icontains="Dinner")
        return context


class BreakfastRecipeList(ListView):
    model = Recipe
    context_object_name = "recipes"
    template_name = "app/recipe_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = context['recipes'].filter(category__icontains="Breakfast")
        return context



class RecipeDetail(DetailView):
    model = Recipe
    context_object_name = "recipe"


class RecipeCreate(CreateView):
    model = Recipe
    success_url = reverse_lazy("recipes")
    template_name = "app/recipe_create.html"
    form_class = RecipeModelForm
    # form_class = RecipeForm


class RecipeUpdate(UpdateView):
    model = Recipe
    success_url = reverse_lazy('recipes')
    template_name = "app/recipe_update.html"
    form_class = RecipeModelForm


class RecipeDelete(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes')
    template_name = "app/recipe_delete.html"




