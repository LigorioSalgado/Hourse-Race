class Horse:

    def __init__(self, name):
        self.name = name
        self.steps = []
        self.win = False

    def set_steps(self, steps):
        """
        Poner (*) dentro del atributo steps del caballo
        """
        for step in range(steps):
            self.steps.append("*")
        print("Caballo %s avanza %d" % (self.name, steps))

    def print_steps(self):
        """
        Imprimir el nombre del caballo y la cantidad de pasos
        """
        print("%s : " % self.name, end="")
        for step in self.steps:
            print("*", end="")
        print()

    def is_winner(self):
        """
        Verifica si la cantidad de pasos del caballo llega a 20
        """
        if len(self.steps) >= 20:
            self.win = True

