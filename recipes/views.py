from telnetlib import STATUS
from turtle import title

from django.db.models import Q
from django.http import Http404  # noqa
from django.shortcuts import get_list_or_404, get_object_or_404, render
from utils.recipes.factory import make_recipe  # noqa

from .models import Recipe


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):

    recipes = get_list_or_404(
        Recipe.objects.filter(category__id=category_id,
                              is_published=True).order_by('-id')
    )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{ recipes[0].category.name }  - Category |',
    })


def recipe(request, id):

    recipe = get_object_or_404(Recipe, pk=id, is_published=True)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        # O or do Mysql é feito dessa forma no Django
        Q(
            Q(title__contains=search_term) |  # esse pipe é o or
            Q(description__icontains=search_term),
        ),
        # Aqui seria o and do MySql
        is_published=True


    ).order_by('-id')

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'recipes': recipes,
    })
