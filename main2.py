notas = input().split()
N1, N2, N3, N4 = map(float, notas)
media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10
print("Media: {:.1f}".format(media))
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input())
    print("Nota do exame: {:.1f}".format(nota_exame))
    media_final = (media + nota_exame) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(media_final))
