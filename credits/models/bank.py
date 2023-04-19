# -*- coding: utf-8 -*-
from django.utils.translation import gettext_lazy as _
from django.db import models

class Bank(models.Model):
    """
    Modelo para describir un Banco
    """
    BANK_TYPE = (
        ('PRV', 'Privado'),
        ('GOB', 'Gobierno'),
    )

    name = models.CharField(_("Nombre"), max_length=50, db_index=True)
    btype = models.CharField(_("Tipo"), max_length=4, choices=BANK_TYPE)
    address = models.TextField(_("Dirección"), blank=True, null=True)
    
    def __str__(self):
        return self.name
