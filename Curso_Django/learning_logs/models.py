from django.db import models

#Criando uma nova tabela
class Topic(models.Model):
    """
    Um assunto sobre o qual o usuário esta aprendendo
    """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """
        DEvolve uma representação em string do modelo.
        """
        return self.text

class Entry(models.Model):
    """
    Anotações sobre um tópico específico existente.
    """
    #Sera um topico especifico existente, caso esse topico seja apagado todas as anotações seram apagadas juntas (on_delete-CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    #USADO PARA CORRIGIR O PLURAL DE ENTRY
    class Meta:
        verbose_name_plural = 'entries'


    def __str__(self):
        """
            Devolve uma representação menor em string do modelo.
        """
        return (
            f"({self.topic.text[:10]}...) {self.text[:50]}..."
            if len(self.topic.text) > 10
            else f"({self.topic.text}) {self.text[:50]}..."
)


