# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 22:08:30 2019
@author: Issac Romero
"""
class trabajador:
    # sueldo: dinero percibido por dia.
    def __init__(self,nombre,sueldo,departamento):
        self.nombre = nombre
        self.sueldo = sueldo
        self.departamento = departamento
        
    def getSueldo(self):
        return self.sueldo 
    def setSueldo(self,sueldo):
        self.sueldo = sueldo
        
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre = nombre
        
    def getDepartamento(self):
        return self.departamento 
    def setDepartamento(self,departamento):
        self.departamento = departamento

    def calcularFaltas(self):
        '''para calcular el numero de faltas 
        1 = asistencias
        0 = faltas '''
        lista = []
        #ingresa el numero de dias que trabaja
        captura=int(input("dias laborables (quincena): "))
        contador=0       
        while captura > contador:
            valor = int(input("Ingrese 1/asistencia o 0/falta: "))
            lista.append(valor)
            contador=contador+1

        print("el numero de faltas son: ",lista.count(0))
                         
    def calcularSalario(self):
        
        faltas = int(input("ingresa el numero de faltas en la quincena: "))
        descuento = self.sueldo*2
        if(faltas == 0):
            salario = self.sueldo*15
            salario_men = (salario*2)
            salario_anual = (salario_men*12)
            
            print("el salario quincenal es: $"+str(salario))
            print("el salario mensual es:   $"+str(salario_men))
            print("el salario anual es:     $"+str(salario_anual))
            print("................................................")
        else:
            print("^^^^salario considerando",faltas," faltas en la primera quicena^^^")
            salario_falta = (self.sueldo*15)- (faltas*descuento)
            salario = self.sueldo*15
            salario_men = (salario*2 - faltas*descuento)
            salario_anual = ((salario*24) - faltas*descuento)
            
            print("el salario quincenal es: $"+str(salario_falta))
            print("el salario mensual es:   $"+str(salario_men))
            print("el salario anual es:     $"+str(salario_anual))
            print("................................................")
            
    def calcularVaca(self):
        años_cap = int(input("años trabajados: "))
        if(años_cap==0):
            print("no tiene vacaciones")
        elif(años_cap==1):
            print("vacaciones corresponde a 6 dias")
        elif(años_cap==2):
            print("vacaciones corresponde a 8 dias")
        elif(años_cap==3):
            print("vacaciones corresponde a 10 dias")
        elif(años_cap==4):
            print("vacaciones corresponde a 12 dias")
        elif(años_cap==5):
            print("vacaciones corresponde a 14 dias")
        elif(años_cap>5):
            print("vacaciones corresponde a 16 dias")    
            
    def printData(self):
        print(self.nombre, self.sueldo, self.departamento)
################################################## ##################          
class operador(trabajador):
    
    def __init__ (self,nombre,sueldo,departamento):
        trabajador.__init__ (self,nombre,sueldo,departamento)
        self.sueldo = sueldo
        print("OPERADOR")
#####################################################################          
class supervisor(trabajador):
    
    def __init__ (self,nombre,sueldo,departamento):
        trabajador.__init__ (self,nombre,sueldo,departamento)
        self.sueldo = sueldo
        print("SUPERVISOR")
 #####################################################################        
class gerente(trabajador):
    
    def __init__ (self,nombre,sueldo,departamento):
        trabajador.__init__ (self,nombre,sueldo,departamento)
        self.sueldo = sueldo
        print("GERENTE")
######################################################################
class director(trabajador):
    def __init__ (self,nombre,sueldo,departamento):
        trabajador.__init__ (self,nombre, sueldo, departamento)
        print("DIRECTOR")
######################################################################
class chofer(trabajador):
    def __init__ (self,nombre,sueldo,departamento):
        trabajador.__init__ (self,nombre, sueldo, departamento)
        print("CHOFER")
#######################################################################
class analista(trabajador):
    def __init__ (self,nombre,sueldo,departamento):
        trabajador.__init__ (self,nombre, sueldo, departamento)
        print("ANALISTA")
#######################################################################
class secretaria(trabajador):
    def __init__ (self,nombre,sueldo,departamento):
        trabajador.__init__ (self,nombre, sueldo, departamento)
        print("SECRETARIA")
#######################################################################
class contador(trabajador):
    def __init__ (self,nombre,sueldo,departamento):
        trabajador.__init__ (self,nombre, sueldo, departamento)
        print("CONTADOR")
        

Trabajador1 = director("Rojas Flores Mariana",2000 ,"Director")
Trabajador2 = gerente("Rosanto Jiménez Armando",500 ,"Gerente")
Trabajador3 = analista("Medina Barber Jennifer Ruth",250 ,"Analista")
Trabajador4 = contador("Suárez Bernal Carlos",250 ,"Contador")
Trabajador5 = supervisor("Rodríguez Almada Jair",200 ,"Supervisor")
Trabajador6 = secretaria("Martínez López María",150 ,"Secretaria")
Trabajador7 = operador("Torres López Angel",120 ,"Operador")
Trabajador8 = operador("Ortega Piedra Ernestina",120 ,"Operador")
Trabajador9 = operador("González Dorantes Sofía",120 ,"Operador")
Trabajador10 = operador("Quintero Arcos Pablo",120 ,"Operador")
Trabajador11 = operador("Aguirre Beltrán Gonzalo",120 ,"Operador")
Trabajador12 = chofer("Hernández Rodríguez Jorge",100 ,"Chofer")
Trabajador13 = chofer("Hernández Malpica Alfredo",100 ,"Chofer")
Trabajador14 = chofer("Bautista Alamillo Juan",100 ,"chofer")