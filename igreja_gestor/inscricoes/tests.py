from django.test import TestCase
from .models import Inscricao
from membros.models import Membro
from eventos.models import Evento

class InscricaoModelTest(TestCase):

    def setUp(self):
        self.membro = Membro.objects.create(
            nome="João da Silva",
            data_nascimento="1990-01-01",
            telefone="123456789",
            email="joao@example.com",
            endereco="Rua A, 123"
        )
        self.evento = Evento.objects.create(
            titulo="Culto de Adoração",
            data="2023-12-01",
            descricao="Um culto especial de adoração.",
            local="Igreja Central"
        )
        self.inscricao = Inscricao.objects.create(
            membro=self.membro,
            evento=self.evento
        )

    def test_inscricao_creation(self):
        self.assertEqual(self.inscricao.membro.nome, "João da Silva")
        self.assertEqual(self.inscricao.evento.titulo, "Culto de Adoração")

    def test_str_method(self):
        self.assertEqual(str(self.inscricao), f"{self.membro.nome} - {self.evento.titulo}")

    def test_inscricao_evento(self):
        self.assertEqual(self.inscricao.evento, self.evento)

    def test_inscricao_membro(self):
        self.assertEqual(self.inscricao.membro, self.membro)