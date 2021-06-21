from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from fst.characters.models import Character


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'wip', 'player', 'name', 'gender', 'age', 'race', 'home_planet', 'allies', 'rank'
            )
        }),
        (_('Description'), {
            'fields': (
                'stigma', 'hair', 'eyes', 'complexion', 'height', 'weight', 'image', 'history'
            )
        }),
        (_('Stats'), {
            'classes': ('collapse',),
            'fields': (
                'max_vitality', 'current_vitality', 'max_wyrd',
                'current_wyrd', 'current_hits', 'experience_points'
            )
        })
    )
