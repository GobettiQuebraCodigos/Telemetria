from django.db import models

# Create your models here.
class Marca(models.Model):
    Nome = models.CharField(max_length=15)

    def __str__(self):
        return self.Nome


class Modelo(models.Model):
    Nome = models.CharField(max_length=15)

    def __str__(self):
        return self.Nome

class UnidadeMedida(models.Model):
    Nome = models.CharField(max_length=15)

    def __str__(self):
        return self.Nome

class Medicao(models.Model):
    Tipo = models.IntegerField()
    UnidadeMedidaId = models.ForeignKey(UnidadeMedida, on_delete=models.DO_NOTHING)

class Veiculo(models.Model):
    Descricao = models.CharField(max_length=30)
    Ano = models.IntegerField()
    Horimetro = models.IntegerField()
    MarcaId = models.ForeignKey(Marca, on_delete=models.DO_NOTHING)
    ModeloId = models.ForeignKey(Modelo, on_delete=models.DO_NOTHING)

class MedicaoVeiculo(models.Model):
    Data = models.DateField()
    Valor = models.DecimalField(max_digits=10, decimal_places=2)
    VeiculoId = models.ForeignKey(Veiculo, on_delete=models.DO_NOTHING)
    MedicaoId = models.ForeignKey(Medicao, on_delete=models.DO_NOTHING)