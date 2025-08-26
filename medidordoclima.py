nota = float(input("Digite a nota do clima (1 a 3): "))

if nota == 1.0: 
   print("clima ruim!")
if nota > 1.0 and nota < 3:
   print("clima mais ou menos.")
else:
   print("clima bom!")
