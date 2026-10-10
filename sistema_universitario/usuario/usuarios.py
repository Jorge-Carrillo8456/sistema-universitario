class Usuarios:
  def __init__(self, nombreU, contrasena, tipoUsuario):
    self.nombreU = nombreU
    self.contrasena = contrasena

    posiblesUsua = ["Alumno", "Profesor", "Empleado"]
    if tipoUsuario in posiblesUsua:
      self.tipoUsuario = tipoUsuario
    else:
      self.tipoUsuario = "Desconocido"
      print("Advertencia: Usuario no valido en la universidad {}".format(self.nombreU))

#En esta parte no supe como pedirlo, pense en crear una lista con 3 nombres, alumno, profesor, empleado,
# que cada cuenta tenga una estructura, por ejemplo, que todos los alumnos empiezen por 1 en su cuenta
# o que los alumnos, su cuenta sea modulo de 2, pero la verdad no supe como implementar esto

  def determinarUsuario(self):
    print("El usuario {} es un {} de la universidad".format(self.nombreU, self.tipoUsuario))


  

