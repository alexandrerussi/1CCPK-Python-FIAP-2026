from pprint import pprint

from aluno import Aluno
from disciplina import Disciplina

# criar 1 aluno
aluno1 = Aluno("Daniel", "123456", "CC")

# criar 2 disciplinas
prompt_ia = Disciplina("IA", "Jorge")
dsa = Disciplina("Data Structures", "Álvaro")

# matricular o aluno nessas 2 disciplinas
aluno1.matricular(prompt_ia)
aluno1.matricular(dsa)

# adicionar notas do aluno em cada disciplina
aluno1.adicionar_nota(prompt_ia, 10)
aluno1.adicionar_nota(prompt_ia, 6)
aluno1.adicionar_nota(dsa, 5)
aluno1.adicionar_nota(dsa, 5)

notas_ia = aluno1.media_por_disciplina(prompt_ia)
# print(notas_ia)

aluno1.exibir_boletim()