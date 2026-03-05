from rest_framework import serializers
from api_telemetria import models

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marca
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador da marca'},
            'Nome': {'help_text': 'Nome da marca'},
        }


class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modelo
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador do modelo'},
            'Nome': {'help_text': 'Nome do modelo'},
        }

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Veiculo
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador do veículo'},
            'Descricao': {'help_text': 'Descrição do veículo'},
            'Ano': {'help_text': 'Ano do veículo'},
            'Horimetro': {'help_text': 'Horímetro do veículo'},
            'MarcaId': {'help_text': 'Identificador da marca. Buscar no GET do API Marca'},
            'ModeloId': {'help_text': 'Identificador do modelo. Buscar no GET do API Modelo'},
        }

class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UnidadeMedida
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador do tipo de unidade de medida'},
            'Nome': {'help_text': 'Tipo de unidade de medida'},
        }

class MedicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medicao
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador da medição'},
            'Tipo': {'help_text': 'Tipo de medição'},
            'UnidadeMedidaId': {'help_text': 'Identificador do tipo de unidade de medida. Buscar no GET do API UnidadeMedida'},
        }

class MedicaoVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicaoVeiculo
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador da medição do veículo'},
            'Data': {'help_text': 'Data da medição do veículo'},
            'Valor': {'help_text': 'Valor da medição do veículo'},
            'VeiculoId': {'help_text': 'Identificador do veículo. Buscar no GET do API Veiculo'},
            'MedicaoId': {'help_text': 'Identificador do tipo de medição. Buscar no GET do API Medicao'},
        }