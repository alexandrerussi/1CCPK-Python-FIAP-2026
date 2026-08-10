# 1. Identificar 1 sucesso

def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

# print(eh_sucesso(200))

# 2. detectando 2 erros seguidos

# [201, 500, 502, 201, 500]
def erros_seguidos(lista_status):
    for i in range(len(lista_status) - 1):
        codigo_atual = lista_status[i]
        prox_codigo = lista_status[i + 1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True

    return False

# print(erros_seguidos(status[1]))

# 3. ANALISANDO UM ENDPOINT COMPLETO
# calcular a porcentagem
# classificar entre critico, instavel e estavel

def analisar_endpoint(lista_status):
    qtd_sucessos = 0

    for codigo in lista_status:
        if eh_sucesso(codigo):
            qtd_sucessos += 1

    qtd_requisicoes = len(lista_status)
    qtd_erros = qtd_requisicoes - qtd_sucessos
    percentual = (qtd_sucessos / qtd_requisicoes) * 100

    tem_erros_seguidos = erros_seguidos(lista_status)

    if tem_erros_seguidos:
        classificacao = "CRÍTICO"
    elif percentual >= 80:
        classificacao = "ESTÁVEL"
    else:
        classificacao = "INSTÁVEL"

    return (
        qtd_sucessos,
        qtd_erros,
        percentual,
        classificacao
    )

endpoints = ["/login", "/produtos", "/pedidos"]

status = [
    [200, 200, 401, 200, 500], # /login
    [200, 200, 200, 200, 200], # /produtos
    [201, 500, 502, 201, 500]
]

# print(endpoints[0])
# print(status[0])

# percorrendo toda a matriz

maior_qtd_erros = 0
endpoint_maior_erro = ""

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    status_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint(status_endpoint)

    print(f"Endpoint: {nome_endpoint}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"Percentual de sucessos: {percentual}")
    print(f"Classificação: {classificacao}")
    print("-" * 30)
    print()

    if erros > maior_qtd_erros:
        maior_qtd_erros = erros
        endpoint_maior_erro = nome_endpoint


print(f"Endpoint com maior nº erros: {endpoint_maior_erro}")
print(f"Qtd erros: {maior_qtd_erros}")