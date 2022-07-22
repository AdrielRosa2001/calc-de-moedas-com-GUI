from os import error, replace
from shutil import Error
from typing import Sized
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import popup, popup_get_text


def convercao_para_exibicao(valor):
    try:
        convertido = valor
        convertido = str(convertido)
        convertido = convertido.replace(".", ",")
        return convertido
    except:
        convertido = "0,00"
        return convertido

def gerar_valor(quantidade, multiplicador, valor_anterior):
    retorno = quantidade * multiplicador
    valor_anterior = valor_anterior + retorno
    return valor_anterior

def fazer_caixa(dinheiro, valores_em_especie):
    resultado = (dinheiro - valores_em_especie) - 100
    return resultado

#variaveis

valor = 0.00
valor_em_especie = 0.00
valor_temporario = 0.00

sg.theme('Reddit')

coluna01 = [
    [sg.Text('Notas de R$ 200', font=('Open'))],
    [sg.Text('Notas de R$ 100', font=('Open'))],
    [sg.Text('Notas de R$ 50', font=('Open'))],
    [sg.Text('Notas de R$ 20', font=('Open'))],
    [sg.Text('Notas de R$ 10', font=('Open'))],
    [sg.Text('Notas de R$ 5', font=('Open'))],
    [sg.Text('Notas de R$ 2', font=('Open'))],
    [sg.Text('Moedas de R$ 1', font=('Open'))],
    [sg.Text('Moedas de R$ 0,50', font=('Open'))],
    [sg.Text('Moedas de R$ 0,25', font=('Open'))],
    [sg.Text('Moedas de R$ 0,10', font=('Open'))],
    [sg.Text('Moedas de R$ 0,05', font=('Open'))],
    [sg.Text('Moedas de R$ 0,01', font=('Open'))],
    
]

coluna02 = [
    [sg.InputText(default_text=('0'), key=('-200-'), size=(5,1), font=('Open'))],
    [sg.InputText(default_text=('0'), key=('-100-'), size=(5,1), font=('Open'))],
    [sg.InputText(default_text=('0'), key=('-50-'), size=(5,1), font=('Open'))],
    [sg.InputText(default_text=('0'), key=('-20-'), size=(5,1), font=('Open'))],
    [sg.InputText(default_text=('0'), key=('-10-'), size=(5,1), font=('Open'))],
    [sg.InputText(default_text=('0'), key=('-5-'), size=(5,1), font=('Open'))],
    [sg.InputText(default_text=('0'), key=('-2-'), size=(5,1), font=('Open'))],
    [sg.InputText(default_text=('0'), key=('-1-'), size=(5,1), font=('Open'))],
    [sg.InputText(default_text=('0'), key=('-0.50-'), size=(5,1), font=('Open'))],
    [sg.InputText(default_text=('0'), key=('-0.25-'), size=(5,1), font=('Open'))],
    [sg.InputText(default_text=('0'), key=('-0.10-'), size=(5,1), font=('Open'))],
    [sg.InputText(default_text=('0'), key=('-0.05-'), size=(5,1), font=('Open'))],
    [sg.InputText(default_text=('0'), key=('-0.01-'), size=(5,1), font=('Open'))]
]

coluna03 = [
    [sg.Text('Valores em Especie:')],
    [sg.InputText('0,00', key=('-valores-'), size=(18, 1)), sg.Button('Adicionar', key=('-adicionar-'))],
    [sg.Text("Ultimo valor adicionado: R$ 0.00", key=('-ultimo_valor_adicionado-'), size=(27,1))],
    [sg.Button('Remover Ultimo', key=('-remover_ultimo-'), size=(14, 1)), sg.Button('Zerar', key=('-zerar_valor-'), size=(8, 1))],
    [sg.Text("VALOR DOS CAIXAS: R$ 0,00", key=('-valor_dos_caixas-'), size=(27,1), text_color='red', font=('Arial Black', 10))],
    [sg.Text("FUNDO DE CAIXA: R$ 100,00", key=('-fundo_de_caixa-'), text_color='red', font=('Arial Black', 10)), sg.Button('+', key=('-+-'))],
    [sg.Text("VALOR TOTAL: R$ 0,00", size=(21,1), key=('-total2-'), text_color='red', font=('Arial Black', 10))],
    [sg.Text("RESULTADO: ", size=(10,1), text_color='red', font=('Arial Black', 8)), sg.Text("", key=('-resultado-'), size=(25,2), text_color='green', font=('Arial Black', 8))]
]

layout = [
    [sg.Image(filename=('logo2.png'))],
    [sg.Column(coluna01), sg.Column(coluna02), sg.Column(coluna03)],
    [sg.Button('Calcular', key=('-calcular-'), size=(7, 1)), sg.Button('Zerar', key=('-zerar-'), size=(7, 1)), sg.Button('Sobre', key=('-sobre-'), size=(7, 1))],
    [sg.Text("VALOR TOTAL: R$ 0,00", key=('-total1-'), size=(24,1), text_color='red', font=('Arial Black', 10))]
]

janela = sg.Window('Calculadora de moedas', layout)

while True:
    eventos, valores = janela.read()
    
    if eventos in (sg.WIN_CLOSED, 'Cancel'):
        break

    if eventos == '-calcular-':

        lista = [(valores['-200-'], 200), (valores['-100-'], 100), (valores['-50-'], 50), (valores['-20-'], 20), (valores['-10-'], 10), (valores['-5-'], 5), (valores['-2-'], 2), (valores['-1-'], 1), (valores['-0.50-'], 0.50), (valores['-0.25-'], 0.25), (valores['-0.10-'], 0.10), (valores['-0.05-'], 0.05), (valores['-0.01-'], 0.01),]

        try:
            for item in lista:

                valor = float(valor)
                valor = gerar_valor(int(item[0]), item[1], valor)
                valor = round(valor, 2)

            valor = ('%.2f' % valor)
            exibicao_de_valor = convercao_para_exibicao(valor)

            janela['-total1-'].update("VALOR TOTAL: R$ "+str(exibicao_de_valor))
            janela['-total2-'].update("VALOR TOTAL: R$ "+str(exibicao_de_valor))

        except Exception as err:
            print(err)
            sg.popup("Houve um erro ao tentar calcular! \nTipo de Erro: "+str(err))

    if eventos == '-zerar-':
        
        valor = 0.00

        campos = ['-200-', '-100-', '-50-', '-20-', '-10-', '-5-', '-2-', '-1-', '-0.50-', '-0.25-', '-0.10-', '-0.05-', '-0.01-']
        
        for item in campos:
            janela[item].update('0')
        janela['-total1-'].update("VALOR TOTAL: R$ 0,00")
        janela['-total2-'].update("VALOR TOTAL: R$ 0,00")
        
        sg.popup('CAMPOS LIMPOS!')
    
    if eventos == '-adicionar-':
        valor_dos_caixas = valores['-valores-']
        valor_dos_caixas = valor_dos_caixas.replace(",", ".")
        valor_dos_caixas = float(valor_dos_caixas)
        valor_em_especie = valor_em_especie + valor_dos_caixas
        valor_temporario = valor_dos_caixas

        valor_dos_caixas = valor_em_especie
        valor_dos_caixas = ('%.2f' % valor_dos_caixas)
        exibicao_de_valor = convercao_para_exibicao(valor_dos_caixas)

        janela['-valor_dos_caixas-'].update("VALOR DOS CAIXAS: R$ "+exibicao_de_valor)
        valor_temporario = ('%.2f' % valor_temporario)
        janela['-ultimo_valor_adicionado-'].update("Ultimo valor adicionado: R$ "+str(valor_temporario))
        janela['-valores-'].update("0,00")

        # aplicando resultado

        resultado_do_caixa = fazer_caixa(float(valor), float(valor_em_especie))
        

        if resultado_do_caixa == 0:
            janela['-resultado-'].update("CAIXA BATEU COM SUCESSO!\n R$ 0,00", text_color=('green'))
        elif resultado_do_caixa > 0:
            resultado_do_caixa = ('%.2f' % resultado_do_caixa)
            resultado_do_caixa = str(resultado_do_caixa)
            resultado_do_caixa = resultado_do_caixa.replace(".", ",")
            janela['-resultado-'].update("SOBRA DE CAIXA: R$ "+resultado_do_caixa, text_color=('red'))
        elif resultado_do_caixa < 0:
            resultado_do_caixa = ('%.2f' % resultado_do_caixa)
            resultado_do_caixa = str(resultado_do_caixa)
            resultado_do_caixa = resultado_do_caixa.replace(".", ",")
            janela['-resultado-'].update("FALTANDO NO CAIXA: R$ "+resultado_do_caixa, text_color=('red'))
        
    if eventos == '-remover_ultimo-':
        valor_em_especie = float(valor_em_especie) - float(valor_temporario)
        valor_dos_caixas = valor_em_especie
        valor_dos_caixas = ('%.2f' % valor_dos_caixas)
        exibicao_de_valor = convercao_para_exibicao(valor_dos_caixas)
        janela['-valor_dos_caixas-'].update("VALOR DOS CAIXAS: R$ "+exibicao_de_valor)

    if eventos == '-zerar_valor-':
        valor_em_especie = 0.00
        valor_temporario = 0.00
        janela['-valor_dos_caixas-'].update("VALOR DOS CAIXAS: R$ 0,00")
        janela['-total2-'].update("VALOR TOTAL: R$ 0,00")
        janela['-resultado-'].update("")

    if eventos == '-+-':
        fundo_de_caixa = popup_get_text("Escreva o valor do fundo de caixa: ")
        print(fundo_de_caixa)

    if eventos == '-sobre-':
        sg.popup('Created By: Adriel ;p\n\nInstagram: @adri3lr00\nGithub: https://github.com/AdrielRosa2001\nTelegram: @AdrielPy\n\nMais informações sobre a aplicação em meu repositório do github.')

janela.close()

