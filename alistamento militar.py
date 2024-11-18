from datetime import date
atual = date.today().year
sexo = input("Se identifica como homem ou mulher: ").strip().lower()

if sexo == "mulher":
    print("Você não tem obrigatoriedade de alistamento militar.")

elif sexo == "homem":
 nasc = int(input("Digite seu ano de nascimento: "))
 idade = atual - nasc
 print(f"Quem nasceu em {nasc} tem {idade} anos em {atual}")
 if idade == 18:
    print("Você está no ano de alistamento!")
 elif idade < 18:
    saldo = 18 - idade 
    print(f"Ainda faltam {saldo} anos para o alistamento")
    ano = atual + saldo
    print(f"Seu alistamento será em {ano}")
 elif idade > 18:
    saldo = idade - 18
    print(f"Você já deveria ter se alistado há {saldo} anos")
    ano = atual - saldo
    print(f"Seu alistamento foi em {ano}")
else:
   print("Entrada inválida.")
