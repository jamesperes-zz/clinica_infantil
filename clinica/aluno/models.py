from django.db import models
from padroes import choices

class Aluno(models.Model):
	nome = models.CharField("Nome", max_length=30,)