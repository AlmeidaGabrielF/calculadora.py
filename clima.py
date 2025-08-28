nota = float(input("Digite a nota do clima (1 a 3): "))

if not nota == 3.0 and 2.0: 
   print("clima ruim!")
if nota > 1.0 and nota < 3:
   print("clima mais ou menos.")
if nota > 2.0:
   print("clima bom!")