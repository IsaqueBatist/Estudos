# Escreva um programa que converta uma temperatura digitada em °C e converta para °F
tempC= float(input('Qual a temperatura em °C?'))
tempF= ((9*tempC)/5) + 32
print('A temperatura de {}°C corresponde a {:1}°F' .format(tempC,tempF))