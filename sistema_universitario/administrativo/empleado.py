class Empleado:
  def __init__(self, nombreE, numCuentaE, puesto, sueldoE, horasTrabajadas, horasExtra):
    self.nombreE = nombreE
    self.numCuentaE = numCuentaE
    self.puesto = puesto
    self.sueldoE = sueldoE
    self.horasTrabajadas = horasTrabajadas
    self.horasExtra = horasExtra

#De igual forma se va a considerar el sistema completamente homogeneo.
#Como en este caso, no son profesores y pueden ser directivos y pueden tener mas o menos horas
# en fines de semana o entre semana, las horas extra y demas, este se calculo directo, peroooo
# las horas extras las vamos a pagar al doble, solo para ver como funciona. 
# si hay 140 dias, de los cuales, digamos que si solo duermen, comen (1 horas por comida) y trabajan
# (2 horas en llegar al trabajo), el maximo de horas que pueden trabajar por dia es de 11 horas.
# si hay 140 dias, como maximo, pueden trabajar 1540 horas, ahora, la jornada laboral es de 8 horas,
# es decir, 1120 horas se puede trabajar el jornada laboral, 420 como horas extra. 

  def calculoSueldoE(self):
    if self.horasTrabajadas<0 :
      print("No puedes trabajar horas negativas")
    elif self.horasExtra<0: 
      print("No puedes trabajar horas negativas")
    elif self.horasTrabajadas > 1120:
      print("No puedes trabajar mas horas de las posibles")
    elif self.horasExtra > 420:
      print("No puedes trabajar mas horas de las posibles")
    else:
      sueldoSemeE = (self.horasTrabajadas * self.sueldoE) + (self.horasExtra * 2 * self.sueldoE)
      sueldoMesE = sueldoSemeE/5
      sueldoSemaE = sueldoMesE/4
      print("El empleado {} con puesto {}, gano {} en todo el semestre".format(self.nombreE , self.puesto, sueldoSemeE))
      print("es decir gano {} por mes".format(sueldoMesE))
      print("es decir gano {} por semana".format(sueldoSemaE))