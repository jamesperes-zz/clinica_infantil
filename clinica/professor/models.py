from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from padroes import choices

class Professor(models.Model):
	#Dados Pessoais
	nome = models.CharField("Nome", max_length = 30)
	cpf = models.CharField("CPF", max_length = 11)
	sexo = models.CharField("Sexo", max_length = 1, choices = choices.SEXO_CHOICES)
	data_nascimento = models.DateField("Data de Nascimento", null = True)

	#Contato
	telefone = models.CharField("Telefone", max_length = 12, null = True)
	email = models.EmailField(null = True)

	#Usuario do Professor
	user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)