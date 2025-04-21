from django.db import models
from django.contrib.auth.models import User

class Topico(models.Model):
    """Um assunto sobre qual o usuario esta aprendendo"""
    text = models.CharField(max_length=200)
    """usa-se CharField para textos pequenos com max_length"""
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Devolve uma representacao em string do modelo lá no painel administrativo"""
        return self.text
    
class Entrada(models.Model):
    """Algo especifico aprendido sobre um determinado assunto"""
    topico = models.ForeignKey(Topico, on_delete= models.CASCADE )
    """o on_delete CASCADE diz que se voce apagar um topico, voce ira apagar todos os campos ligados a ele."""
    text = models.TextField()
    """usa-se TextField para textos grandes, sem limites de caracteres"""
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50] + '...'