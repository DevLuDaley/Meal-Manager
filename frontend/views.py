# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic.detail import DetailView

from meals.models import Meal
from recipes.models import Recipe
from ingredientLists.models import IngredientList
from ingredients.models import Ingredient


def index(request):
    return render(request, 'frontend/index.html')


class MealDetailView(DetailView):
    model = Meal
    template_name = 'frontend/index.html'