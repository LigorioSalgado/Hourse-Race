import random


class Race:

    turno = 1

    def __init__(self, horse1, horse2):
        self.horse1 = horse1
        self.horse2 = horse2

    def start(self):
        while(len(self.horse1.steps) < 20 and len(self.horse2.steps) < 20):
            print("Turno %d" % self.turno)

            # Primer Caballo
            self.horse1.set_steps(random.randrange(5))
            self.horse1.is_winner()

            # Segundo Caballo
            self.horse2.set_steps(random.randrange(5))
            self.horse2.is_winner()

            # Imprimir pasos
            self.horse1.print_steps()
            self.horse2.print_steps()
            self.turno += 1
        self.end()

    def end(self):
        print("====== Termino la carrera ======")
        self.winner()

    def winner(self):
        print("====== Ganador ======")
        if self.horse1.win and self.horse2.win:
            print("%s y %s Empataron!!!" % (
                self.horse1.name, self.horse2.name))
        elif self.horse1.win:
            print(self.horse1.name)
        else:
            print(self.horse2.name)