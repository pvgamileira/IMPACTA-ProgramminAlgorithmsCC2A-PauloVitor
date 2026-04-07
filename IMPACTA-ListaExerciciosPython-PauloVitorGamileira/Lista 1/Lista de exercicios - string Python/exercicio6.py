data = input("Digite uma data no formato dd/mm/aaaa: ")

dia = data[0:2]
mes = data[3:5]
ano = data[6:10]

mes_extenso = ""
if mes == "01":
    mes_extenso = "Janeiro"
elif mes == "02":
    mes_extenso = "Fevereiro"
elif mes == "03":
    mes_extenso = "Março"
elif mes == "04":
    mes_extenso = "Abril"
elif mes == "05":
    mes_extenso = "Maio"
elif mes == "06":
    mes_extenso = "Junho"
elif mes == "07":
    mes_extenso = "Julho"
elif mes == "08":
    mes_extenso = "Agosto"
elif mes == "09":
    mes_extenso = "Setembro"
elif mes == "10":
    mes_extenso = "Outubro"
elif mes == "11":
    mes_extenso = "Novembro"
elif mes == "12":
    mes_extenso = "Dezembro"

print(dia + " de " + mes_extenso + " de " + ano)
