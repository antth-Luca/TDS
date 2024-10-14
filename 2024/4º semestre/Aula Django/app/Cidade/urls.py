from django.urls import path
from .views import CreateCidadeView, ListCidadeView, EditCidadeView

urlpatterns = [
    path('cadastro-cidade', CreateCidadeView.as_view(), name='CreateCidade'),
    path('listar-cidade', ListCidadeView.as_view(), name='ListCidade'),
    path('edit-cidade/<int:pk>', EditCidadeView.as_view(), name='EditCidade'),
]
