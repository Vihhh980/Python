temperatura = int(input('Digite a temperatura'))
if temperatura < 16:
  print('Frio')
elif temperatura > 16 and temperatura <25:
  print("Normal")
elif temperatura > 25 and temperatura <30:
  print("Quente")
else:
  print("INFERNO")