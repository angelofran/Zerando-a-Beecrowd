notas = list(map(lambda x: round(float(x), 1), input().split()))
pesos = [2, 3, 4, 1]
soma = 0

for n, p in zip(notas, pesos):
    soma += (n * p)

média = soma / 10

print(f'Media: {média:.1f}')

if média >= 7.0:
    print('Aluno aprovado.')

if média < 5.0:
    print('Aluno reprovado.')

if 5.0 <= média <= 6.9:
    print('Aluno em exame.')
    nota_exame = round(float(input()), 1)
    print(f'Nota do exame: {nota_exame:.1f}')
    média = (média + nota_exame) / 2

    if média >= 5.0:
        print('Aluno aprovado.')

    if média < 5.0:
        print('Aluno reprovado.')
    
    print(f'Media final: {média:.1f}')
