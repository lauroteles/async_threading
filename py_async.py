import datetime
import math
import asyncio

def main():
    print("Iniciando processamento...")

    el = asyncio.get_event_loop()
    inicio = datetime.datetime.now()    

    tarefa1 = el.create_task(computar(inicio = 1, fim = 10_000_000))
    tarefa2 = el.create_task(computar(inicio = 10_000_001 , fim = 20_000_000))
    tarefa3 = el.create_task(computar(inicio = 20_000_001 , fim = 30_000_000))
    tarefa4 = el.create_task(computar(inicio = 30_000_001 , fim = 40_000_000))
    tarefa5 = el.create_task(computar(inicio = 40_000_001 , fim = 50_000_000))

    tarefas = asyncio.gather(tarefa1, tarefa2, tarefa3, tarefa4, tarefa5)

    el.run_until_complete(tarefas)
    tempo = datetime.datetime.now() - inicio

    print(f"Processamento finalizado em {tempo.total_seconds()} segundos")

async def computar(inicio: int, fim: int):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt(abs(pos - fator) * (pos + fator))
      
if __name__ == '__main__':
    main()





''' forma 1 Tempo de execução: 7.30 segundos '''

