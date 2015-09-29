#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from  kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager,Screen
import time
from kivy.uix.label import Label
from tool  import fechas
import random
 
"""
	POr investigar
	como usar los Popup para usarlo validar campos
	como ponemos visualizar en formade tabla los datos a imprimir y consultar
	buscar como hacer para enviar los datos  procesados
""" 

class User(ScreenManager):
	nombre = ObjectProperty()
	empresa = ObjectProperty()
	calendario = fechas()

	#necesitamos POpup para confirmacion y validacion de datos	
	
	div=	ObjectProperty()
	cat=	ObjectProperty()
	subcat=	ObjectProperty()
	med=	ObjectProperty()
	marca=	ObjectProperty()
	sku=	ObjectProperty()
	resultado_lista= ObjectProperty()
	
	espera = []
	add ={}
	temp =[]
	sav = False 
	fin = True
	def iniciar(self):
		self.fecha= self.calendario[0]
		self.hora= self.calendario[1]	
		self.resultado_lista.item_strings = ["NO HAY DATOS PROCESADOS ACTUALMENTE"]	
		print("Inicando...")	
	def categoria(self,consulta, screen):
		self.var_consul = consulta
		self.name = screen
		print("Consultando...")	
	def limpiar(self,):
		self.div.text=self.cat.text=self.subcat.text=self.med.text=self.marca.text =self.sku.text=""
		temp= espera = []
		print("-Limpiando")
	def usuario(self):
		name = (self.nombre.text).strip()
		empresa = (self.empresa.text).strip()
		estado = (self.empresa.text).strip()
		#usu = name+empresa+fecha+hora
		if (name != "" and empresa != ""): estado="usuario--Bien"; print(estado)
		elif name == "" and empresa != "": estado="usuario--Falta Nombre";print("Falta Nombre")
		elif empresa == "" and name != "": estado="usuario--Falta Empresa";print("Falta Empresa")
		else: print("usuario-- Falta usuario")
	
	def save_new_sku(self): #funcion nos servira para guardar la data ingresada
		#asignamos los valores temporablemente a una lista
		temp =[self.div.text,self.cat.text,self.subcat.text,self.med.text,self.marca.text , self.sku.text]
		self.espera =[]
		self.espera = temp
		#agragamos a la lista los valores ingresados		
		if "" in self.espera:
			print("save_new_sku-- Datos Vacios o Incorrectos")
		else:
			self.sav = True			
			print(self.temp)
			print("save_new_sku-- Datos Correctos")
			self.fin = False
	def save(self): #funcion nos servira para guardar la data ingresada
		
		# self.espera =[]
		temp =[self.div.text,self.cat.text,self.subcat.text,self.med.text,self.marca.text , self.sku.text]
		
		#agragamos a la lista los valores ingresados
		if self.fin == False:
			for x in temp:
		 		self.espera.append(x)
		 	print(self.espera)
		 	print("save-- Datos Correctos")
		else:
			print("save-- Datos Vacios o Incorrectos")
		# for x in temp:
		# 	self.espera.append(x)
		# if "" in self.espera:
		# 	print("save-- Datos Vacios o Incorrectos")
		# else:
		# 	#clave id  y los valores serial temp
						
		# 	print(self.add)
		# 	print("save-- Datos Correctos")
	def save_db(self,):
		if self.sav == False:
			print("save_db-- No Procesados base da datos")
		else:	
			id = random.getrandbits(10)
			self.add[id]=self.espera
			self.resultado_lista.item_strings = ["{0}, {1}".format(clave,valor) for clave,valor in self.add.items()]
			print(self.add)
			print("save_db--Actualizar base da datos")		

class ReportesApp(App):
	title = 'reportes'
	icon = 'icon.png'
 
	def build(self):  
		return User()
	def on_pause(self):
		return True



if __name__ == '__main__':
	ReportesApp().run()
