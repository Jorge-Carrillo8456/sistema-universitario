class Alumno:
  def __init__(self, nombre, numCuenta, carerra, semestre, numAsistencia, numInscritas):
    self.nombre = nombre
    self.numCuenta = numCuenta
    self.carrera = carerra
    self.semestre = semestre
    self.numAsistencia = numAsistencia
    self.numInscritas = numInscritas

  def mostrar(self):
    print("Nombre Alumno : {}".format(self.nombre))
    print("Numero de Cuenta : {}".format(self.numCuenta))
    print("Carrera : {}".format(self.carrera))
    print("Semestre : {}".format(self.semestre))
    print("Numero de Asistencia : {}".format(self.numAsistencia))
    print("Numero de Materias Inscritas : {}".format(self.numInscritas))

#Vamos a homogeneizar el sistema para facilitar su calculo a atravez de las siguientes reglas. 
#1.- El semestre dura 5 meses de clases, el otro es de vacaciones, cada mes tiene exactamente 28 dias
#es decir, 4 semenas exactas, por ende, son 140 dias, pero, justamente 40 dias son de fin de semana
#vamos a suponer que no hay clases sabatinas, asi pues, solo evaluamos 100 dias exactos.
#2.- Si el individuo registra asistencia, vamos a asumir que hizo todos sus deberes, si tenia 3 clases 
#un dia y tuvo asistencia, entro a esas 3 clases. 
#3.- Cada clase dura 2 horas, el calculo de creditos por materia, es el numero de horas que se le tiene 
#que dedicar por semana, por ejemplo, si una materia tiene 8 creditos, implica que a la semana se
#impartieron 4 clases. 

  def derechoExamen(self):
    asistencia = self.numAsistencia
    if asistencia >= 80 :
      print("El alumno {} tiene derecho a examen en sus materias".format(self.nombre))
      return True
    else:
      print("El alumno {} NO tiene derecho a examen en sus materias".format(self.nombre))
      return False

#Añadir el :list, fue ayuda de IA para dar indicaciones
  def ingresarCalif(self, listaCalif: list):
    if len(listaCalif) == self.numInscritas:
      self.listaCalif = listaCalif
      return True
    else: 
      return False

  def calcularProm(self, listaCalif: list):
    if self.ingresarCalif(listaCalif)==True:
      sum = 0
      for i in self.listaCalif:
        sum = sum + i
      prom = sum/len(self.listaCalif)
      print("El promedio final del alumno {} es de {}".format(self.nombre, prom))
    else:
      print("No se pudo calcular el promedio de forma exitosa")