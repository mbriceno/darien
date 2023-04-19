# -*- coding: utf-8 -*-
from django.utils.translation import gettext_lazy as _
from django.db import models

class Credit(models.Model):
    """
    Model to describe a Credit for a user
    """
    CREDIT_TYPE = (
        ('AUTO', 'Automotriz'),
        ('HIPO', 'Hipotecarios'),
        ('COMER', 'Comerciales'),
    )

    client = models.ForeignKey("commons.Client", verbose_name=_("Cliente"), on_delete=models.CASCADE)
    bank = models.ForeignKey("credits.Bank", verbose_name=_("Banco que otorgante"), on_delete=models.CASCADE)
    description = models.TextField(_("Dirección"))
    credit_amount = models.DecimalField(_("Monto del crédito"), max_digits=16, decimal_places=2)
    min_payment = models.DecimalField(_("Pago Mínimo"), max_digits=16, decimal_places=2)
    max_payment = models.DecimalField(_("Pago Máximo"), max_digits=16, decimal_places=2)
    credit_term = models.PositiveIntegerField(_("Plazo del Crédito"), help_text=_("Plazo en Meses"), db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    ctype = models.CharField(_("Tipo de Crédito"), max_length=5, choices=CREDIT_TYPE)
    
    def __str__(self):
        return "{} - {}".format(self.client, self.bank)
