from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({"cpf": "CPF invalido"})

        if not nome_valido(data['nome']):
            serializers.ValidationError({"nome": "o nome deve conter apenas letras"})

        if not rg_valido(data['rg']):
            serializers.ValidationError({"rg": "o RG deve ter 9 digitos"})

        if not celular_valido(data['celular']):
            serializers.ValidationError({"celular": "o ccelular deve ter 11 digitos"})

        return data

    # def validate_cpf(self, cpf):
    #     if len(cpf)!=11:
    #         raise serializers.ValidationError("o cpf deve ter 11 digitos")
    #
    #     return cpf
    #
    # def validate_nome(self, nome = str()):
    #     if not nome.isalpha():
    #         raise serializers.ValidationError("o nome deve conter apenas letras")
    #
    #     return nome
    #
    # def validate_rg(self, rg):
    #     if len(rg)!=9:
    #         raise serializers.ValidationError("o RG deve ter 9 digitos")
    #
    #     return rg
    #
    # def validate_celular(self, celular):
    #     if len(celular)<11:
    #         raise serializers.ValidationError("o ccelular deve ter 11 digitos")
    #
    #     return celular