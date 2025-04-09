from django.urls import path
from . import views
"""esse . diz que estou importando o arquivo views que esta dentro dessa mesma pasta """
"""poderia substituir esse . pelo nome da pasta "aprendizadopythons" """

urlpatterns = [
    path('', views.index, name='index'),
    path('topicos', views.topicos, name='topicos' ),
    path('topico/<topico_id>/', views.topico, name='topico'),
    path('novo_topico', views.novo_topico, name='novo_topico'),
    path('nova_anotacao/<topico_id>/', views.nova_anotacao, name='nova_anotacao'),
    path('edit_entrada/<entrada_id>', views.edit_entrada, name='edit_entrada'),
    path('delete_entrada/<entrada_id>', views.delete_entrada, name='delete_entrada'),
]

"""index é uma funcao que crio dentro de views"""
