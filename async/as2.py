import datetime
import asyncio

async def gerar_dados(quantidade: int, dados: asyncio.Queue):
    print(f'Gerando {quantidade} dados')
    for idx in range(1, quantidade + 1):
        item = idx * idx
        await dados.put((item, datetime.datetime.now()))
        await asyncio.sleep(0.001)
    print(f'{quantidade}  -- > Dados gerados Com sucesso')        

async def consumir_dados(quantidade : int ,dados: asyncio.Queue):
    print(f'Aguarde o processamento {quantidade} dados...')
    processados = 0
    while processados < quantidade:
        item = await dados.get()
        print(f'Processando {item}...')
        processados += 1
        await asyncio.sleep(0.001)
        print(f'{item} processado com sucesso')

async def main():
    total = 5000
    dados = asyncio.Queue()
    print(f'Iniciando processamento...  {total * total:.2f}')

    await gerar_dados(total, dados)
    await gerar_dados(total, dados)
    await consumir_dados(total * 2, dados)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()    

