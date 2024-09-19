print ("Clase V2 Roberto Vazquez")

#Zona de clase
class Datos:
    # el constructor funcion
    def __init__(self,estatura,peso):
        self.estatura=estatura
        self.peso=peso
    def mostrar_datos(self):
        print(f"Estatura: {self.estatura} mts, Peso: {self.peso} kg")
    print ("LISTA")
    def mi_lista(self):
        mains=["Sonic", "Hero", "Toon Link", "Sora", "Falco", "Mii Swordfighter"]
        print(mains)
        for x in mains:
            print (x)
    def mi_tupla(self):
        print ("TUPLA")
        games = ("64", "Melee", "Brawl", "Sm4sh", "Ultimate")
        print(games)
        for z in games:
            print(z)
    def mi_set(self):
        print ("SET")
        counters = {"King DDD", "Joker", "Sephiroth", "Inkling", "Lucina", "Steve", "Fox", "Terry", "Kazuya", "Mii Fighter", "Mii Swordfighter", "Mii Gunner", "Marth", "Ganon"}
        print(counters)
        for y in counters:
            print(y)
    def mi_diccionario(self):
        print("DICCIONARIO")
        fort = {
        "Skin": "Rubius",
        "Style": "MadKat",
        "Backpack": "Wilson"
    }
        print(fort)
        for x, y in fort.items():
            print(x, y)

#Creacion de peso
info=Datos(1.75,70)

# Utilizando el Obj.
info.mostrar_datos()
info.mi_lista()
info.mi_tupla()
info.mi_set()
info.mi_diccionario()