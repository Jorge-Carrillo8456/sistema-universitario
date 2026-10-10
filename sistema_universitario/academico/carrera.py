class Carrera:
  def __init__(self, nombreC, claveC,):
    self.nombreC = nombreC
    self.claveC = claveC
    self.lisMateria = []

  def agregar_materia(self, materia):
        self.lisMateria.append(materia)
        print("Materia agregada exitosamente a la carrera {}".format(self.nombreC))