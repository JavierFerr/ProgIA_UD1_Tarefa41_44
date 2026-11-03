# Para esta tarefa imos a precisar: - Unha función que aplique un 21% de IVE a unha cantidade 
# Unha función que aplique un 4% de IVE a unha cantidade - Unha función que aplique un 10% de desconto a unha cantidade.

# Finalmente vas a ter unha lista coa lista da compra. Para elemento da lista será un dicionario onde haberá:

#     prezo do produto sen IVE
#     unha función que aplica o desconto… ou None en caso de non ter desconto
#     unha función que calcule o IVE do produto

# Crearás unha función que colla unha cesta da compra e nos devolve o total a pagar
# o IVE da compra e máis a cantidade obtida de aplicar os descontos.

# Xera os tes unitarios correspondentes.

def aplicar21IVE(cant):
    return cant * 1.21

def aplicar4IVE(cant):
    return cant * 1.04

def aplicar10desc(cant):
    return cant * 0.9

def totalCesta(lista):
    total = 0
    ive = 0
    desconto = 0

    for productos in lista:
        prezo_sen_ive = productos["prezo_sen_ive"]
        aplicar_desconto = productos["desconto"]
        prezo_con_desconto = (
            prezo_sen_ive
            if aplicar_desconto is None
            else aplicar_desconto(prezo_sen_ive)
        )
        prezo_con_ive = productos["calcular_ive"](prezo_con_desconto)

        total += prezo_con_ive
        ive += prezo_con_ive - prezo_con_desconto
        desconto += prezo_sen_ive - prezo_con_desconto

    return total, ive, desconto


lista_da_compra = [
    {
        "produto": "Pan",
        "prezo_sen_ive": 1.20,
        "desconto": None,
        "calcular_ive": aplicar21IVE,
    },
    {
        "produto": "Aceite de oliva",
        "prezo_sen_ive": 8.50,
        "desconto": aplicar10desc,
        "calcular_ive": aplicar21IVE,
    },
    {
        "produto": "Deterxente",
        "prezo_sen_ive": 6.00,
        "desconto": None,
        "calcular_ive": aplicar21IVE,
    },
    {
        "produto": "Leite",
        "prezo_sen_ive": 0.95,
        "desconto": None,
        "calcular_ive": aplicar4IVE,
    },
]


if __name__ == '__main__':
    lista = totalCesta(lista_da_compra)
    print(f"Total: {round(lista[0],2)}")
    print(f"IVE: {round(lista[1],2)}")
    print(f"Desconto: {round(lista[2],2)}")