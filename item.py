class item :
    def __init__(self, name, description, strength, protect ):
        self.name=name
        self.strength=strength
        self.protect=protect
        self.description = description
    def __str__(self):
        return f"Vous avez pris {self.name}, {self.description}, avec une masse de {self.weight}"
        pass
   
    #instancier les objets

    Epee1=item("Dague Mortelle","Ajoute 30 de défense et 20 d'attaque",2)
    Epee2=item("Dague Mortelle","Ajoute 30 de défense et 20 d'attaque",2)