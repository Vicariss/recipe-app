from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Recipe, Category
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import RecipeModelForm

# Create your views here.


class RecipeList(ListView):
    model = Recipe
    template_name = "app/recipe_list.html"
    context_object_name = "recipes"
    paginate_by = 7
    ordering = ["-publish_date"]

    def get_queryset(self, *args, **kwargs):
        search_input = self.request.GET.get('search') or ''
        choose_category = self.request.GET.get('choose-category')
        
        if choose_category:
            return Recipe.objects.filter(category__icontains=choose_category).order_by("publish_date")

        if search_input:
            return Recipe.objects.filter(
                Q(name__icontains=search_input) | Q(requirements__icontains=search_input) | Q(description__icontains=search_input)).order_by("publish_date")

        return super().get_queryset(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        choose_category = self.request.GET.get('choose-category')
        search_input = self.request.GET.get('search') or ''
        if search_input:
            context["search_input"] = search_input
        if choose_category:
            context["choose_category"] = choose_category
            
        context['categories'] = Category.objects.all()
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




