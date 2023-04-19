# -*- coding: utf-8 -*-
from django.utils.translation import gettext_lazy as _
from django.db import models

class Client(models.Model):
    """
    Modelo para describir un client del sistema
    """
    CLIENT_TYPE = (
        ('NTR', 'Natural'),
        ('JRD', 'Juridico'),
    )
    full_name = models.CharField(_("Nombre"), max_length=50, db_index=True)
    birthdate = models.DateField(_("Fecha Nacimiento"), db_index=True)
    years_old = models.PositiveIntegerField(_("Edad"), db_index=True)
    nationality = models.CharField(_("Nacionalidad"), max_length=50, db_index=True, blank=True, null=True)
    address = models.TextField(_("Dirección de habitación"), blank=True, null=True)
    email = models.EmailField(_("Email"), max_length=254)
    phone = models.CharField(_("Teléfono"), max_length=50, blank=True, null=True)
    ptype = models.CharField(_("Tipo de Persona"), max_length=4, choices=CLIENT_TYPE)
    bank = models.ForeignKey("credits.Bank", verbose_name=_("Banco"), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.full_name
