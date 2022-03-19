
from django import forms
from recipes.models import Recipe
from utils.django_forms import add_attr, add_placeholder


class AuthorRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        add_attr(self.fields.get('preparation_steps'), 'class', 'span-2')
        add_attr(self.fields.get('cover'), 'class', 'span-2')
        add_placeholder(self.fields['title'], 'Your recipe title')
        add_placeholder(self.fields['description'], 'Your recipe description')

    class Meta:
        model = Recipe
        fields = [
            'title',
            'description',
            'preparation_time',
            'preparation_time_unit',
            'servings',
            'serving_unit',
            'preparation_steps',
            'cover',
        ]

        widgets = {
            'cover': forms.FileInput(
                attrs={
                    'class': 'span-2'
                }
            ),

            'serving_unit': forms.Select(
                choices=(

                    ('Porções', 'Porções'),
                    ('Pedaços', 'Pedaços'),
                    ('Pessoas', 'Pessoas'),

                ),
            ),

            'preparation_time_unit': forms.Select(
                choices=(

                    ('Minutos', 'Minutos'),
                    ('Horas', 'Horas'),

                ),
            ),
        }
