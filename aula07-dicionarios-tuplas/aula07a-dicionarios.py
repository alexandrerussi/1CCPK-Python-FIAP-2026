eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {
    'one': 'uno',
    "two": "dos",
    "three": "tres"
}
print(eng2sp)
print(eng2sp["two"])
print(len(eng2sp))

# OPERADOR IN
# ele acusa se algo aparecer como chave no dict
print('one' in eng2sp)

# values()
valores_dict = eng2sp.values()
print('uno' in valores_dict)

print()

### CONTADOR DE LETRAS
def count_letters(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

count = count_letters("paralelepipedo")
print(count)
