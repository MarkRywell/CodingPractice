# Problem 16
# Gasoline Shit

print("Fuel Type                    Amount / Liter")
print()
print("(R)egular                    P 41.85")
print("(U)nleaded                   P 40.45")
print("(P)remium                    P 42.50")
print("(D)iesel                     P 34.15")
print()
select_fuel = input("Select Fuel: ")

fuel = {

    'R': 41.85,
    'U': 40.45,
    'P': 42.50,
    'D': 34.15
}

fuel = fuel.get(select_fuel)

print()

print("(C)ash")
print("(L)iter")
print()
option = input("Select Option: ")
print()

if option == 'C':
    amount = float(input("Enter amount: P "))
    final = amount / fuel
    print("No. of Liters Dispensed: ", round(final, 2))
elif option == 'L':
    amount = float(input("Enter amount: L "))
    final = amount * fuel
    print("Amount of Payment: ", round(final, 2))





