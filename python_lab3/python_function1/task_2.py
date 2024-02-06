# fahrenheit_temperature = float(input())

def fahrenheit_to_centigrade(temperature):
    C = (5 / 9) * (temperature - 32.0)
    return C

print(fahrenheit_to_centigrade(fahrenheit_temperature))
