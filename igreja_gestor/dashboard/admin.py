from django.contrib import admin
from .models import DashboardModel  # Substitua pelo modelo real que você irá usar

# Registra os modelos do dashboard no painel administrativo
@admin.register(DashboardModel)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ('campo1', 'campo2', 'campo3')  # Substitua pelos campos reais do seu modelo
    search_fields = ('campo1', 'campo2')  # Substitua pelos campos que deseja pesquisar
    list_filter = ('campo3',)  # Substitua pelos campos que deseja filtrar

# Adicione outras configurações administrativas conforme necessário