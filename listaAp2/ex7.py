def calcular_temperatura(celsius, fahrenheit):
    fahrenheit_form = (celsius * 1.8) + 32
    return fahrenheit_form


celsius = float(input("Digite uma temperatura em celsius: "))
fahrenheit = float(input("Digite uma temperatura em fahrenheit: "))

print(
    f"A temperâtura transformada de celsius para fahrenheit é de: {calcular_temperatura(celsius, fahrenheit)}"
)
