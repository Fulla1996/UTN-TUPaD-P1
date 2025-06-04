class Productos:
    def __init__(self):
        self.productos_y_stock = {}

    def agregarProd(self, prod, stock=0):
        self.productos_y_stock[prod] = stock

    def agregarStock(self, prod, stock):
        self.productos_y_stock[prod] = max(0, stock + self.productos_y_stock[prod])
    
    def consultarStock(self, prod):
        return self.productos_y_stock[prod]
    
    def existe(self, prod):
        return prod in self.productos_y_stock
    
stock_de_productos = Productos()
print("Bienvenido")
while True:
    print("\n\t1 - Agregar un producto nuevo o incrementar stock\n\t2 - Consultar el stock\n\t0 - Salir")
    
    op = input("Ingrese la opción deseada: ")
    match op:
        case "1":
            prod = input("Que producto desea agregar? : ").lower()
            cant = int(input("Cuantos desea agregar? : "))
            if stock_de_productos.existe(prod):
                stock_de_productos.agregarStock(prod, cant)
            else:
                stock_de_productos.agregarProd(prod, cant)
        case "2":
            prod = input("Que producto desea consultar? : ").lower()
            if (stock_de_productos.existe(prod)):
                print(f"Stock: {stock_de_productos.consultarStock(prod)}")
            else:
                print("El producto no existe")
        case "0":
            break

print("Vuelva pronto!")