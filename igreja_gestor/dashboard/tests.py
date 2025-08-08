from django.test import TestCase
from django.urls import reverse
from .models import Dashboard

class DashboardTests(TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        self.dashboard = Dashboard.objects.create(
            # Adicione os campos necessários para criar um objeto Dashboard
        )

    def test_dashboard_view(self):
        # Testa se a view do dashboard está acessível
        response = self.client.get(reverse('dashboard:index'))  # Altere 'dashboard:index' para o nome correto da URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/index.html')  # Altere para o template correto

    def test_dashboard_data(self):
        # Testa se os dados do dashboard estão corretos
        response = self.client.get(reverse('dashboard:index'))  # Altere 'dashboard:index' para o nome correto da URL
        self.assertContains(response, self.dashboard.some_field)  # Altere 'some_field' para um campo relevante

    def tearDown(self):
        # Limpeza após os testes
        self.dashboard.delete()