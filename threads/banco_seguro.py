import threading
import random
import time
from colorama import Fore, Style
from typing import List

''' Fazer utilização do Rlock para evitar que a thread seja interrompida durante a execução de um bloco de código'''

lock = threading.RLock()
class Conta:
    def __init__(self, saldo: float) -> None:
        self.saldo = saldo


def main():
    contas = criar_contas()

    with lock:
        total = sum(conta.saldo for conta in contas)
    
    print(Fore.GREEN + 'Inicado trasnferências...')
    taferas = [
        threading.Thread(target=servicos, args=(contas, total)),
        threading.Thread(target=servicos, args=(contas, total)),
        threading.Thread(target=servicos, args=(contas, total)),
        threading.Thread(target=servicos, args=(contas, total)),
        threading.Thread(target=servicos, args=(contas, total)),
        
    ]
    [tarefa.start() for tarefa in taferas]
    [tarefa.join() for tarefa in taferas]

    print(Fore.GREEN + 'Transferências finalizadas')
    valida_banco(contas, total)

def servicos(contas,total):
    for _ in range(1,10_000):
        c1,c2 = pega_duas_contas(contas)
        valor = random.randint(1,100)
        transferir(c1,c2,valor)
        valida_banco(contas,total)

def criar_contas () -> List[Conta]:
    return [
        Conta(saldo=random.randint(1,1000)),
        Conta(saldo=random.randint(1,1000)),
        Conta(saldo=random.randint(1,1000)),
        Conta(saldo=random.randint(1,1000)),
        Conta(saldo=random.randint(1,1000)),
        
    ]            

def transferir(conta_origem: Conta, conta_destino: Conta, valor: float) -> None:

    with lock:
        if conta_origem.saldo >= valor:
            conta_origem.saldo -= valor
            conta_destino.saldo += valor
            print(Fore.LIGHTBLUE_EX + f'Transferência de {valor} realizada com sucesso')
        else:
            print(Fore.RED + 'Saldo insuficiente')

def valida_banco(conta: List[Conta],total: int):
    with lock:
        atual = sum(conta.saldo for conta in conta)
    
    if atual != total:
        print(Fore.RED + f'ERRO: saldo inconsistente {atual} != {total}')
    else:
        print(Fore.GREEN + 'Saldo consistente',total)

def pega_duas_contas(contas: List[Conta]) -> List[Conta]:
    c1,c2 = random.sample(contas,2)
    return c1,c2


if __name__ == "__main__":
    main() 