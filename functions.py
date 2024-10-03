# Declaramos las funciones a utilizar en el programa
mortgage = " "
monthly_earning = 0
def users_data():
    global mortgage
    global monthly_earning
    
    print("Hola bienvenido a Spent Monthly, porfavor ingrese lo siguiente: ")
    user = input("Nombre: ")
    edad = input("Edad: ")
    
    while True:
        try:
            edad = int(edad)
            break  # Sale del bucle si la conversión a entero es exitosa
        except ValueError:
            print("Por favor, ingrese una edad válida.")
        edad = input("Edad: ")

    while True:
        mortgage = input("¿Cuenta con una renta o crédito hipotecario? ").lower()
        if mortgage in ["si", "no"]:
            break
        else:
            print("Por favor, ingrese una opción válida (si o no).")
    
    monthly_earning = input("Por favor, ingrese sus ingresos mensuales: ")
    while True:
        try:
            monthly_earning = float(monthly_earning)
            break
        except ValueError:
            print("Por favor, ingrese un monto válido.")
        monthly_earning = input("Ingrese sus ingresos mensuales: ")


"""
This function calculates the total expenses based on the monthly expenses provided by the user.

Parameters:
None

Returns:
total_expenses (float): The total expenses calculated based on the monthly expenses.
"""
monthly_expenses = {}
total_expenses = 0
def economics_data():
    
    options = ["continuar", "no", "si", "salir"]
    option = " "
    global monthly_expenses
    
    monthly_expenses = {}
    
    print("Porfavor ingrese las gastos mensuales: ")
    while option != "salir":
    
        monthly_expenses.update({input("Gasto: "): input("Monto: ")})
        # Pendiente de arreglar el while
        option = input("Desea agregar otro gasto? ").lower()
        if option == "si":
            option = "continuar"
        elif option == "no":
            print("Tus gastos mensuales son: ", monthly_expenses)
            option = "salir"
        elif option not in options:
            print("Porfavor ingrese una respuesta valida [si/no].")
            option = input("Desea agregar otro gasto? ").lower()
        total_expenses = sum(float(value) for value in monthly_expenses.values())
    
    print("Tus gastos totales son: ", total_expenses)
    
    return total_expenses

"""
Calculate the percentage of monthly expenses relative to monthly earnings.

This function takes no parameters and uses global variables `monthly_earning` and `monthly_expenses`.
It calculates the total expenses by summing the values of the `monthly_expenses` dictionary.
The percentage of expenses relative to earnings is then calculated by dividing the total expenses by the monthly earnings and multiplying by 100.
The income percentage is calculated by subtracting the expense percentage from 100.

This function prints the expense and income percentages as strings and returns the expense percentage as a floating-point number.
"""

def percentage():
    global monthly_earning
    global monthly_expenses
    monthly_earning = float(monthly_earning)
    total_expenses = sum(float(value) for value in monthly_expenses.values())
    
    percentage = (total_expenses/monthly_earning) * 100
    income_percentage = (100 - percentage)
    
    print("Tus gastos representan el: " + str(percentage) + "% " + "de tus ingresos mensuales.")
    print("Te queda sobrante de tus ingresos mensuales: " + str(income_percentage) + "% ")
    print("Presiona cualquier boton para regresar al menu")
    return percentage

"""
Calculate the monthly budget based on the monthly earning and mortgage status.

This function takes no parameters.

Returns:
float: The monthly earning.

Raises:
None.
"""
def montly_budget():
    global monthly_earning
    global mortgage
    monthly_earning = float(monthly_earning)
    if mortgage == "si":
        mortgage_budget = (monthly_earning * 0.4)
        personal_budget = (monthly_earning * 0.1)
        inversion_budget = (monthly_earning * 0.2)
        expenses_budget = (monthly_earning * 0.3)
        print("El presupuesto mensual que tiene este mes es de: ")
        print("Inversión: " + str(inversion_budget)) 
        print("Personal: " + str(personal_budget))
        print("Hipoteca: " + str(mortgage_budget))
        print("Gastos: " + str(expenses_budget))
        print("Presiona cualquier boton para regresar al menu")
    elif mortgage == "no":
        personal_budget = (monthly_earning * 0.2)
        inversion_budget = (monthly_earning * 0.3)
        expenses_budget = (monthly_earning * 0.3)
        emergency_budget = (monthly_earning * 0.2)
        print("El presupuesto mensual que tiene este mes es de: ")
        print("Inversión: " + str(inversion_budget)) 
        print("Personal: " + str(personal_budget))
        print("Gastos: " + str(expenses_budget))
        print("Fondo de Emergencia: " + str(emergency_budget))
        print("Presiona cualquier boton para regresar al menu")
    return monthly_earning
