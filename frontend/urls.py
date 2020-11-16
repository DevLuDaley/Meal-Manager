from django.urls import path

from .views import index, MealDetailView, RecipeViewSet, IngredientListViewSet, IngredientViewSet

urlpatterns = [
    # path('', index),
    # path('edit/<int:pk>', MealDetailView.as_view()),
    # path('delete/<int:pk>', MealDetailView.as_view()),
]