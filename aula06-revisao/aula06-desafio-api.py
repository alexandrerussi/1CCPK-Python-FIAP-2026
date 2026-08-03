endpoints = ["/login", "/produtos", "/pedidos"]

status = [
    [200, 200, 401, 200, 500], # /login
    [200, 200, 200, 200, 200], # /produtos
    [201, 500, 502, 201, 500]
]

# print(endpoints[0])
# print(status[0])

# 1. Identificar 1 sucesso

def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

# print(eh_sucesso(401))

# 2. detectando 2 erros seguidos

def erros_seguidos(lista_status):
    for i in range(len(lista_status) - 1):
        codigo_atual = lista_status[i]
        prox_codigo = lista_status[i + 1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True

    return False

print(erros_seguidos(status[2]))