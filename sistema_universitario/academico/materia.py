class Materia:
  def __init__(self, nombreM, clave, numCreditosM):
    self.nombreM = nombreM
    self.clave = clave
    self.numCreditosM = numCreditosM
    self.profImpartida = []
  #Esto self lo agregue para componer los otros metodos, ya que al crear una materia, esta nace sin 
  #alumnos cursandola. 
    self.aluCursando=0

  def agregar_profesor(self, profesor):
        self.profImpartida.append(profesor)
        print("Profesor agregado exitosamente a la materia {}".format(self.nombreM))

  #Como el programa es muy pequeño (Solo vamos a usar a lo mucho 3 materias, 3 profesores y 3 alumnos)
  # vamos a adaptar el sistema para que sea asi en la realidad, en la vida real un profesor puede tener 
  # hasta 50 alumnos por salon, pero nos vamos a reducir a que esta es una escuela especial y solo hay 
  # un cupo por profesor, para poder crear casos donde hay y donde no hay cupos, si se quiere probar
  #basta con cambiar el valor del parametro.

  def cupoM(self):
    i = len(self.profImpartida)
    j = abs(self.aluCursando-len(self.profImpartida))
    if i>self.aluCursando:
      print("Hay cupo suficiente")
      print("Hay {} sobrantes".format(j))
      return True
    elif i==self.aluCursando:
      print("Hay cupo suficiente")
      print("NO hay mas espacios")
      return False
    elif i<self.aluCursando:
      print("NO hay cupo suficiente")
      print("Faltan {} espacios".format(j))
      return False

  def registrarAlumno(self):
    if self.cupoM()==True:
      self.aluCursando = self.aluCursando + 1
    else:
      print("No hay cupo disponible para registrar al alumno :(")

#No me pidieron esta funcion, pero es basicamente la misma de registrar alumno, solo que con un signo
#negativo y cambiarle el nombre
  def bajarAlumno(self):
      if self.aluCursando==0:
        print("No puedes dar de baja alumnos si no hay nadie inscrito XD")
      else:
        self.aluCursando = self.aluCursando - 1
        