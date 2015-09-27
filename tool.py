#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
fechas.py - Genera un diccionario con datos utiles sobre fecha y hora actuales.
'''

import datetime

diasemana = {'MONDAY':'Lunes','TUESDAY':'Martes','WEDNESDAY':'Miercoles',
             'THURSDAY':'Jueves','FRIDAY':'Viernes','SATURDAY':'Sabado',
             'SUNDAY':'Domingo'}

mes = {'JANUARY':'Enero','FEBRUARY':'Febrero','MARCH':'Marzo',
       'APRIL':'Abril','MAY':'Mayo','JUNE':'Junio',
       'JULY':'Julio','AUGUST':'Agosto','SEPTEMBER':'Setiembre',
       'OCTOBER':'Octubre','NOVEMBER':'Noviembre','DECEMBER':'Diciembre'}

def fechas():
    '''
    Devuelve un diccionario con las siguientes claves:
    fecha : Fecha actual en formato 'datetime.date'
    fechora : Fecha y hora actuales en formato 'datetime.date'
    hora : Hora actual en formato 'str'
    dia : Dia de la semana segun diccionario en formato 'str'
    mes : Mes actual segun diccionario en formato 'str'
    '''
    dic = {}
    dic['fecha'] = datetime.date.today()
    dic['fechora'] = datetime.datetime.today()
    dic['hora'] = dic['fechora'].time().__str__().split('.')[0]
    dic['dia'] = diasemana[dic['fecha'].strftime('%A').upper()]
    dic['mes'] = mes[dic['fecha'].strftime('%B').upper()]
    
    fecha = "{0} {1} de {2} del {3}".format(dic['dia'],dic['fecha'].day,dic['mes'],dic['fecha'].year)
    hora = ""+dic['hora']
    fecha = [fecha, hora]

    return fecha

# d = fechas()
# print("fecha ",d[0],"hora ",d[1])