from django.db import models

# Create your models here.

class AparelhoManager(models.Manager):
    
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(potencia__icontains=query))

class Aparelho(models.Model):
    name = models.CharField(verbose_name='Nome do aparelho', max_length=100)
    slug = models.SlugField(verbose_name='Atalho')
    potencia = models.IntegerField(verbose_name='Potencia em watts', null=True, blank=True)
    tempo = models.IntegerField(verbose_name='Tempo sugerido',null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    objects = AparelhoManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'aparelho'
        verbose_name = 'aparelho'
        verbose_name_plural = 'Aparelho'
        ordering = ['name']

