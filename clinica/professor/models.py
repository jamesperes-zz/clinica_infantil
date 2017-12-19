from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from padroes import choices

class Professor(models.Model):
	#Dados Pessoais
	nome = models.CharField("Nome", max_length = 30)
	cpf = models.CharField("CPF", max_length = 11)
	genero = models.CharField("Gênero", max_length = 1, choices = choices.GENERO_CHOICES)
	data_nascimento = models.DateField("Data de Nascimento")
	#Contato
	telefone = models.CharField("Telefone", max_length = 12)
	email = models.EmailField()
	#Usuario do Professor
	user = models.OneToOneField(User, on_delete = models.CASCADE)