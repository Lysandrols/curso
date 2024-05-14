class OrdemDeServico:
    def __init__(self, cliente, descricao, data, tecnico):
        self.cliente = cliente
        self.descricao = descricao
        self.data = data
        self.tecnico = tecnico

    def __str__(self):
        return f"Ordem de Serviço\nCliente: {self.cliente}\nDescrição: {self.descricao}\nData: {self.data}\nTécnico: {self.tecnico}"

def gerar_ordem_de_servico():
    cliente = input("Informe o nome do cliente: ")
    descricao = input("Descreva o serviço a ser realizado: ")
    data = input("Informe a data (DD/MM/AAAA): ")
    tecnico = input("Informe o nome do técnico responsável: ")

    ordem_de_servico = OrdemDeServico(cliente, descricao, data, tecnico)
    return ordem_de_servico

# Exemplo de uso:
if __name__ == "__main__":
    ordem_de_servico = gerar_ordem_de_servico()
    print(ordem_de_servico)
