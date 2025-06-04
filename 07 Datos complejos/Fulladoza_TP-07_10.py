capitales = {"Argentina": "Buenos Aires", "Chile" : "Santiago"}
invertido = {}
for key, value in capitales.items():
    invertido[value] = key

print(invertido)