from django.test import TestCase
from .models import Membro

class MembroModelTest(TestCase):

    def setUp(self):
        Membro.objects.create(
            nome="João da Silva",
            data_nascimento="1990-01-01",
            telefone="123456789",
            email="joao@example.com",
            endereco="Rua A, 123",
            status="ativo"
        )

    def test_membro_criado(self):
        membro = Membro.objects.get(nome="João da Silva")
        self.assertEqual(membro.telefone, "123456789")
        self.assertEqual(membro.status, "ativo")

    def test_membro_inativo(self):
        membro = Membro.objects.create(
            nome="Maria Oliveira",
            data_nascimento="1985-05-05",
            telefone="987654321",
            email="maria@example.com",
            endereco="Rua B, 456",
            status="afastado"
        )
        self.assertEqual(membro.status, "afastado")