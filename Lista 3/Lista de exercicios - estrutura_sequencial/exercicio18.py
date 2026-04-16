tamanho_arquivo = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_internet = float(input("Digite a velocidade do link de Internet (em Mbps): "))

# Conversor de Mbps para MBps dividindo por 8
# Segundos = tamanho em MB dividido pela velocidade em MB/s
velocidade_em_MBs = velocidade_internet / 8
tempo_segundos = tamanho_arquivo / velocidade_em_MBs
tempo_minutos = tempo_segundos / 60

print(f"O tempo aproximado de download sera de {tempo_minutos} minutos.")
