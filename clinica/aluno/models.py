from django.db import models
from django.contrib.auth.models import User
from padroes import choices

class Aluno(models.Model):
	#Dados Pessoais
	nome = models.CharField("Nome", max_length = 30, null = True)
	cpf = models.CharField("CPF", max_length = 11, null = True)
	sexo = models.CharField("Sexo", max_length = 1, choices = choices.SEXO_CHOICES, null = True)
	data_nascimento = models.DateField("Data de Nascimento", null = True)

	#Dados Academicos
	matricula = models.CharField("Matrícula", max_length = 11, null = True)

	#Contato
	telefone = models.CharField("Telefone", max_length = 12, null = True)
	email = models.EmailField(null = True)

	#Status
	aprovado = models.BooleanField(default=False)

	#User
	user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)