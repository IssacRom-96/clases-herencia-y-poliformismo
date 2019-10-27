# Clases, herencia y polimorfismo :family:  :computer:

Ejercicio de como aplicar las propiedades de la programación orientada a objetos:
- Clases
- Herencia
- Polimorfismo

## Consideraciones
Crear la clase "TRABAJADOR" con los atributos: nombre, sueldo, departamento.
Métodos: calcularSalario, calcularFaltas,calcularRetardos.
Clases derivadas: obrero, supervisor, gerente.

## Entradas (inputs) y salidas (outputs)
Entrada: excel con los datos: nombres, calfs/ventas, carrera/depto, etc.
Salida: análisis de la informacion, promedios/ventas/salarios y graficas
                 
## EJEMPLO
Se ingresa trabajador1 = obrero("nombre",sueldo(diario),departamento)
                       supervisor(mismos atributos)                                                        
                       gerente(mismos atributos)
               
Una vez ingresado el trabajador para la clase deseada, podemos calcular
las faltas de la siguiente manera:
       -ingresar trabajador1.calcularFaltas()
        esta opcion te pedira el numero de dias laborables, 
        es decir, ingresas un 15 ya que manejamos quincenas
       -ahora crearás la lista de 15 datos con ceros y unos
        que equivalen a 1-->asistencias, 0-->faltas
       -esto te dara el valor del numero de faltas                

Para calcula el salario:
        -ingresar trabajador1.calcularSalario()
        esta funcion te pedira ingresar el numero anterior de 
        faltas
        -al ingresarlo imprime el total del salario quincenas

Este mismo procedimiento se puede hacer para n número de trabajadores,
se puede ingresar los datos aquí o en la terminal de python.

TRABAJADOR1 = operador("JUAN",200,"produccion")
TRABAJADOR1.calcularFaltas()
TRABAJADOR1.calcularSalario()

TRABAJADOR2 = supervisor("hector",400,"produccion")
TRABAJADOR2.calcularFaltas()
TRABAJADOR2.calcularSalario()

TRABAJADOR3 = gerente("issac",600,"CIO")
TRABAJADOR3.calcularFaltas()
TRABAJADOR3.calcularSalario()