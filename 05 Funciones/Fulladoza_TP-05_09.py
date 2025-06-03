def celsius_a_fahrenheit(celsius):
    return (celsius * (9/5)) + 32

c = float(input("Ingrese la temperatura en Celsius: "))

print(f"{c}° Celsius equivalen a {celsius_a_fahrenheit(c):.2f}° Fahrenheit")