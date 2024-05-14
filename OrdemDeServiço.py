import sys

class OrdemDeServico:
    def __init__(self, empresa, cliente, descricao, valor, data, tecnico):
        self.empresa = empresa
        self.cliente = cliente
        self.descricao = descricao
        self.valor = valor
        self.data = data
        self.tecnico = tecnico

    def __str__(self):
        return f"Ordem de Serviço\nEmpresa: {self.empresa}\nCliente: {self.cliente}\nDescrição: {self.valor}\nValor: {self.descricao}\nData: {self.data}\nTécnico: {self.tecnico}"

def gerar_ordem_de_servico():
    empresa = input("Informe o nome da empresa: ")
    cliente = input("Informe o nome do cliente: ")
    descricao = input("Descreva o serviço a ser realizado: ")
    valor = input("Informe o valor: ")
    data = input("Informe a data (DD/MM/AAAA): ")
    tecnico = input("Informe o nome do técnico responsável: ")

    ordem_de_servico = OrdemDeServico(empresa, cliente, descricao, valor, data, tecnico)
    return ordem_de_servico

def salvar_ordem_de_servico(ordem_de_servico, arquivo):
    with open(arquivo, 'w') as f:
        f.write(str(ordem_de_servico))

# Exemplo de uso:
if __name__ == "__main__":
    ordem_de_servico = gerar_ordem_de_servico()
    arquivo = 'ordem_de_servico.txt'  # Nome do arquivo onde será salvo o resultado
    salvar_ordem_de_servico(ordem_de_servico, arquivo)
    print(f"A ordem de serviço foi salva em {arquivo}")

    # Abrir o Whatsapp, escolher o cliente e enviar ao mesmo

    # Solicita ao usuário pressionar uma tecla antes de fechar
    input("Pressione Enter para sair...")


numero1 = 1
numero2 = 2
numero3 = 3
soma = 1 + 2 + 3
print(soma)