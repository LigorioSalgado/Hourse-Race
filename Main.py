from Horse import Horse
from Race import Race

name_horse1 = input("Nombre del primer caballo: ")
name_horse2 = input("Nombre del segundo caballo: ")

horse1 = Horse(name_horse1)
horse2 = Horse(name_horse2)

race = Race(horse1, horse2)

race.start()