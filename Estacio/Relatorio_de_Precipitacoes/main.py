#import pandas
import os
import glob

try:
    os.mkdir('meio-dia')
except FileExistsError as erro:
    print(erro)

ano: os.DirEntry
for ano in os.scandir('Dados'):
    #print('Diretório Ano:', ano.path)
    try:
        meses = os.scandir(ano.path)
        for mes in meses:
            #print("Diretório Mês:", mes.name)
            #print(f'{mes.path}\\*12')
            for caminho in glob.glob(f'{mes.path}\\*12'):
                try:
                    # print(f'{caminho}')
                    # print(caminho.split('\\'))
                    nome = caminho.split('\\')[3]
                    #move o arquivo para outro diretório
                    os.rename(caminho, f'meio-dia/{nome}')
                    #copia o arquivo para outro diretório
                    #shutil.copy2(caminho, f'meio-dia/{nome}')
                except FileExistsError as erro:
                    print(erro)
    except NotADirectoryError as erro:
        print(erro)

total_medicoes = 0
lat_lon_max = {}
lat_lon_soma = {}
for item in os.scandir('meio-dia'):
    total_medicoes += 1
    #print(item)
    with open(item) as arquivo:
        for line in arquivo:
            dados = line.strip().split()
            lat_lon_max[f'{dados[0]},{dados[1]}'] = max(lat_lon_max.get(f'{dados[0]},{dados[1]}', 0), float(dados[2]))
            lat_lon_soma[f'{dados[0]},{dados[1]}'] = lat_lon_soma.get(f'{dados[0]},{dados[1]}', 0) + float(dados[2])

# for lat_lon, prec in lat_lon_max.items():
#     linha = f'[{lat_lon}] - {prec:.2f}mm - {lat_lon_soma[lat_lon]:.2f}mm'
#     print(linha)
with open('saida.csv', 'w') as saida:
    saida.writelines("--------------+--------+----------\n")
    saida.writelines("Latit.,Longt. | Precip | Somatoria\n")
    saida.writelines("--------------+--------+----------\n")

with open('saida.csv', 'a') as saida:
    for lat_lon, prec in lat_lon_max.items():
        linha = f'[{lat_lon}] | {prec:.2f}mm | {lat_lon_soma[lat_lon]:.2f}mm\n'
        saida.write(linha)