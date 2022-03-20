from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeListViewHome.as_view(), name="home"),  # home
    path('recipes/search/', views.RecipeSearch.as_view(), name="search"),
    path('recipes/category/<int:category_id>/',
         views.RecipeCategory.as_view(), name="category"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),

]
