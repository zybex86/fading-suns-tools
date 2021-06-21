from django.db import models
from django.utils.translation import gettext_lazy as _

from fst.fst.models import BaseModel


class Gender:
    MALE = 'M'
    FEMALE = 'F'
    UNKNOWN = 'U'

    CHOICES = (
        (MALE, _('Male')),
        (FEMALE, _('Female')),
        (UNKNOWN, _('Unknown')),
    )


class Character(BaseModel):
    name = models.CharField(_('name'), max_length=128)
    player = models.CharField(_('player'), max_length=128)
    max_vitality = models.SmallIntegerField(_('max_vitality'))
    current_vitality = models.SmallIntegerField(_('current_vitality'))
    max_wyrd = models.SmallIntegerField(_('max_wyrd'))
    current_wyrd = models.SmallIntegerField(_('current_wyrd'))
    rank = models.CharField(_('rank'), max_length=128, blank=True)
    allies = models.CharField(_('alies'), max_length=512, blank=True)
    stigma = models.CharField(_('stigma'), max_length=128, blank=True)
    race = models.CharField(_('race'), max_length=128, blank=True)
    age = models.SmallIntegerField(_('age'))
    gender = models.CharField(_('gender'), max_length=1, choices=Gender.CHOICES)
    home_planet = models.CharField(_('home_planet'), max_length=128, blank=True)
    hair = models.CharField(_('hair'), max_length=128, blank=True)
    eyes = models.CharField(_('eyes'), max_length=128, blank=True)
    complexion = models.CharField(_('complexion'), max_length=128, blank=True)
    height = models.CharField(_('height'), max_length=128, blank=True)
    weight = models.CharField(_('weight'), max_length=128, blank=True)
    image = models.TextField(_('image'))
    history = models.TextField(_('history'))
    experience_points = models.SmallIntegerField(_('experience_points'))
    current_hits = models.SmallIntegerField(_('current_hits'))
    wip = models.BooleanField(_('wip'), default=True)

    def __str__(self):
        wip = 'WIP' if self.wip else ''
        return f'{self.player} - {self.name} ({wip})'

    class Meta:
        verbose_name = _('character')
        verbose_name_plural = _('characters')
