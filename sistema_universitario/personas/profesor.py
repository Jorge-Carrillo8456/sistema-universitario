class Profesor:
  def __init__(self, nombreP, numCuentaP, departamento, sueldoP, numAsistenciaP, numHoras):
    self.nombreP = nombreP
    self.numCuentaP = numCuentaP
    self.departamento = departamento
    self.sueldoP = sueldoP
    self.numAsistenciaP = numAsistenciaP
    self.numHoras = numHoras

  def mostrarP(self):
    print("Nombre Profesor : {}".format(self.nombreP))
    print("Numero de Cuenta : {}".format(self.numCuentaP))
    print("Departamento : {}".format(self.departamento))
    print("Sueldo : {}".format(self.sueldoP))
    print("Numero de Asistencia : {}".format(self.numAsistenciaP))
    print("Numero de Horas : {}".format(self.numHoras))

#De igual forma se va a considerar el sistema completamente homogeneo.
#Ya paso el semestre, si se asisten un dia, se asistenten a todas las clases o jornada laboral
# 100 dias de trabajo realmente, vamos a considerar que los fines de semana tampoco trabajan
# el sueldo es lo que le pagan por hora y el numero de horas, son las horas que le dieron por dia. 

  def calculoSueldoP(self):
    if self.numAsistenciaP<0:
      print("No puedes tener asistencia negativa")
    elif self.numAsistenciaP>100:
      print("No puedes tener mas asistencia de la que hubo")
    else:
      sueldoSeme = self.numHoras * self.numAsistenciaP * self.sueldoP
      sueldoMes = sueldoSeme/5
      sueldoSema = sueldoMes/4
      print("El profesor {}, gano {} en todo el semestre".format(self.nombreP ,sueldoSeme))
      print("es decir gano {} por mes".format(sueldoMes))
      print("es decir gano {} por semana".format(sueldoSema))