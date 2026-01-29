velocidade = 65
local_carro = 99

RADAR_1 = 60  # velocidade para aplicação da multa
LOCAL_1 = 100  # Local onde o radar esta
RADAR_RANGE = 1 # A Distância onde o radar pega

carro_multado = (LOCAL_1 - RADAR_RANGE) <= local_carro <= (LOCAL_1 + RADAR_RANGE) and \
                velocidade > RADAR_1

if velocidade > RADAR_1:
    print("Velocidade carro passou do radar 1")

if carro_multado:
    print("Carro multado no radar 1")

