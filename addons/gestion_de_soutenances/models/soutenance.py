# -*- coding: utf-8 -*-
from odoo import models, fields

class Soutenance(models.Model):
    _name = "gestion.soutenance"
    _description = "Soutenance"

    name = fields.Char(string="Titre de la soutenance", required=True)
    etudiant = fields.Char(string="Nom de l'etudiant", required=True)
    encadrant = fields.Char(string="Encadrant")
    date_soutenance = fields.Date(string="Date de la soutenance")
    salle = fields.Char(string="Salle")
    statut = fields.Selection([
        ("planifiee", "Planifiee"),
        ("en_cours", "En cours"),
        ("terminee", "Terminee"),
    ], string="Statut", default="planifiee")
    description = fields.Text(string="Description")
