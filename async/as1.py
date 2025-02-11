import datetime
import asyncio

async def gerar_dados(quantidade: int, dados: asyncio.Queue):
    print(f'Gerando {quantidade} dados')
    for idx in range(1, quantidade + 1):
        item = idx * idx
        await dados.put((item, datetime.datetime.now()))
        await asyncio.sleep(1)
    print(f'{quantidade}  -- > Dados gerados Com sucesso')        

async def consumir_dados(quantidade : int ,dados: asyncio.Queue):
    print(f'Aguarde o processamento {quantidade} dados...')
    processados = 0
    while processados < quantidade:
        item = await dados.get()
        print(f'Processando {item}...')
        processados += 1
        await asyncio.sleep(2)
        print(f'{item} processado com sucesso')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    dados = asyncio.Queue()
    gerar = gerar_dados(5000, dados)
    consumir = consumir_dados(5000, dados)
    loop.run_until_complete(asyncio.gather(gerar, consumir))
    loop.close()        