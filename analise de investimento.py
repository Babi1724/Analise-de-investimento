valor_de_investimento=float(input("informe o valor de investimento: "))
CDI=float(input("insira o valor de rentabilidade de CDI: ")) #13,65%
CDB=float(input("insira o valor de rentabilidade de CDB: ")) #12,83%
Tesouro_Direto=float(input("insira o valor de rentabilidade do tesouro direto: ")) #9,94%
Poupança=float(input("insira o valor de rentabilidade da poupança: ")) #0,5%

Primeira_rentabilidade=valor_de_investimento * 1.12
Segunda_rentabilidade=valor_de_investimento * 12.83
Terceira_rentabilidade= valor_de_investimento * 9.94
Quarta_rentabilidade= valor_de_investimento * 0.05

#print(f"o valor da primeira rentabilidade é:{Primeira_rentabilidade}")
#print(f"o valor da segunda rentabilidade é:{Segunda_rentabilidade}")
#print(f"o valor da terceira rentabilidade é:{Terceira_rentabilidade}")
#print(f"o valor da quarta rentabilidade é:{Quarta_rentabilidade}")

if Primeira_rentabilidade>Segunda_rentabilidade:
    print(f"o valor da primeira rentabilidade do CDI é:{Primeira_rentabilidade}")

elif Segunda_rentabilidade>Terceira_rentabilidade:
    print(f"o valor da segunda rentabilidade do CDB é:{Segunda_rentabilidade}")

elif Terceira_rentabilidade>Quarta_rentabilidade:
    print(f"o valor da terceira rentabilidade do tesouro direto é:{Terceira_rentabilidade}")

elif Quarta_rentabilidade>Primeira_rentabilidade:
    print(f"o valor da quarta rentabilidade da poupança é:{Quarta_rentabilidade}")
