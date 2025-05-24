import json
import qrcode
import re

def erro_entrada(entrada, qtdAlternativas):
    alternativas_validas = list(range(1, qtdAlternativas + 1))

    while True:
        try:
            entrada = int(entrada)
            if entrada in alternativas_validas:
                return entrada
            else:
                entrada = input(f"Entrada inválida. Digite um número entre 1 e {qtdAlternativas}: ")
        except ValueError:
            entrada = input("Insira apenas valores numéricos: ")

def validar_placa():
    padrão_placa = r'^[A-Z]{3}[0-9][A-Z0-9][0-9]{2}$'
    while True:
        placa = input("Digite a placa da moto (formato: ABC1D23): ").upper()
        if re.fullmatch(padrão_placa, placa):
            return placa
        else:
            print("Placa inválida! Certifique-se de que segue o padrão Mercosul (ex: ABC1D23).")

def validar_chassi():
    padrão_chassi = r'^[A-HJ-NPR-Z0-9]{17}$'
    while True:
        chassi = input("Digite o chassi da moto (17 caracteres): ").upper()
        if re.fullmatch(padrão_chassi, chassi):
            return chassi
        else:
            print("Chassi inválido! Deve conter exatamente 17 caracteres alfanuméricos (sem I, O ou Q).")

modelos = ("Mottu Sport", "Honda Pop 110I", "Mottu Sport ESD")
setores = (
    "Pronta para aluguel", "Pendente", "Sem placa", "Danos estruturais graves",
    "Reparo simples", "Agendada para manutenção", "Motor defeituoso", "Minha Mottu"
)

placa = validar_placa()
chassi = validar_chassi()

modelo = input(
    "Digite o modelo da moto:\n"
    "1 - Mottu Sport\t2 - Honda Pop 110I\t3 - Mottu Sport ESD\n\n"
)
modelo = erro_entrada(modelo, len(modelos))
modelo = modelos[modelo - 1]

setor = input(
    "Digite o setor da moto:\n"
    "1 - Pronta para aluguel\n2 - Pendente\n3 - Sem placa\n4 - Danos estruturais graves\n"
    "5 - Reparo simples\n6 - Agendada para manutenção\n7 - Motor defeituoso\n8 - Minha Mottu\n\n"
)
setor = erro_entrada(setor, len(setores))
setor = setores[setor - 1]

infoMoto = {
    "placa": placa,
    "chassi": chassi,
    "modelo": modelo,
    "setor": setor
}

json_string = json.dumps(infoMoto)
print(json_string)

qr = qrcode.make(json_string)
qr.save("qrcode.png")