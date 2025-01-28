#Prosty_Kalkulatro
#Alan Włudarski
liczba1 = float(input("Podaj liczbe nr 1: "))
op = input("Podaj liczbe nr 1: ")
liczba2 = float(input("Podaj liczbe nr 2: "))
if op == "+":
  print(liczba1 + liczba2)
elif op == "-":
  print(liczba1 - liczba2)
elif op == "*":
  print(liczba1 * liczba2)
elif op == "/":
  print(liczba1 / liczba2)
else:
  print("Nieprawidłowy operator")
