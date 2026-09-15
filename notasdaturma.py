#As notas de uma turma foram registradas assim: 
#notas = [8.5, 6.0, 9.2, 4.5, 7.0, 5.5, 10.
#0, 3.8, 6.9, 7.5] A partir delas, monte duas novas listas:
# uma com os aprovados (nota ≥ 7) e outra
#com os reprovados.#
notas:list[float] = [8.5, 6.0, 9.2, 4.5, 7.0, 5.5, 10.0, 3.8, 6.9, 7.5]
aprovados: list[float] = []
reprovados:list[float] = []

for i in notas:
    if i <7:
        reprovados.append(i)

        
