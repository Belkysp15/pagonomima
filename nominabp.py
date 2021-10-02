import os
import sqlite3 
#Declaracion de variables ordenadas por orden alfabetico
array7 = []
bono1 = 0
bono_general1 = 0
cedula = 0
emp = []
empleado = 0
fecha_ingreso = 0
horas_extras = 0
salario = 0
salario_base = 0
salario_base2 = 0
#Se crea el archivo que va guardar los calculos de los bonos
archivo2=open("C:/Users/BP/Documents/python nomina/pago_nomina_12sep2021.py","w")
archivo2.write("Cedula****Fecha Ingreso******Empleado***********************Sueldo Base*****Horas Extras*****Monto a Pagar\n")
#Coloco el titulo en color verde 
from colorama import Fore, init
init()
print(Fore.GREEN + "NOMINA DE LA EMPRESA YABADABADU")
#importo los parametros relacionado con los bonos
from script_pago_nomina import *
#Leo el archivo nomina.txt
with open('C:/Users/BP/Documents/python nomina/nomina.txt','r') as archivo:
     linea = archivo.readline()
     print("lista",len(linea))
     while linea != '':
        
        print(Fore.RED + "**********************************************")
        print(Fore.GREEN + "RESUMEN DE NOMINA")
        linea = archivo.readline()
        array7 = linea
        array = []
        array = array7.split( )

        cedula = array[0].lower().replace(' ', '')
        print("Cedula: ",cedula)
        fecha_ingreso = array[1].lower().replace(' ', '')
        fecha_f = []
        fecha_f = fecha_ingreso.split('/')
        print("Fecha Ingreso: ",fecha_f[2],"-",fecha_f[1],"-",fecha_f[0])
        ff = fecha_f[2],"-",fecha_f[1],"-",fecha_f[0]
        emp = array[2],array[3]
        print("Empleado: ",array[2],(""),array[3])
        print("Salario Base: ",array[4])
        salario_base = array[4].lower().replace('$', ' ') #Quita los espacios en vacio de la cadena string de la variable creada
        salario_base2 = int(salario_base)
        bono1 = salario_base2 * Bono_General
        bono_general1 =  bono1
        horas_extras = int(array[5])
        print("Horas Extras: ",horas_extras)
        bono_eficiencia = 0
        print ("Bono General:",bono_general1)
#Valido las horas de los trabajadores para el calculo del bono de eficiencia
        if horas_extras > 5: #Bono Eficiencia
          bono_eficiencia1 = salario_base2*Bono_Eficiencia
          print ("Bono Eficienca:",bono_eficiencia1)
        else:
          print ("Bono Eficienca:",bono_eficiencia1)

        salario = salario_base2 + bono_general1 + bono_eficiencia1
        print ("Sueldo:",salario,"$")
 #Guardo los datos de los calculos       
        archivo2.write(str (cedula) +"***"+ str (fecha_ingreso)+"*********"+ str (emp)+"***********"+ str (salario_base)+"$***************"+ str (horas_extras)+"***************"+ str (salario)+"$\n")
#Cierro los archivos       
archivo.close()
archivo2.close()
  
        
    
        
    
