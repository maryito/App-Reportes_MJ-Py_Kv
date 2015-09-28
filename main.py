#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from  kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager,Screen
import time
from kivy.uix.label import Label
from tool  import fechas

#me quede sobre pensando en cargar los 

class User(ScreenManager):
	nombre = ObjectProperty()
	empresa = ObjectProperty()
	calendario = fechas()

	def horario(self):
		self.fecha= self.calendario[0]
		self.hora= self.calendario[1]
	def categoria(self,consulta, screen):
		self.var_consul = consulta
		self.name = screen	

	def usuario(self):
		name = (self.nombre.text).strip()
		empresa = (self.empresa.text).strip()
		
		if (name != "" and empresa != ""):
			print("Bien")
			# self.status =""
			# print("Usuario: "+name, "Ventana: "+self.status)
		elif name == "" and empresa != "":
			print("Falta Nombre")
		elif empresa == "" and name != "":
			print("Falta Empresa")
		else:
			print("Falta")
			# self.status = "usu"
			# print("Usuario: "+name, "Ventana: "+self.status)
	#necesitamos POpup para confirmacion y validacion de datos	
	espera = ["hoaass","111111",4444]
	div=	ObjectProperty()
	cat=	ObjectProperty()
	subcat=	ObjectProperty()
	med=	ObjectProperty()
	marca=	ObjectProperty()
	sku=	ObjectProperty()
	search_results_list= ObjectProperty()
	def save_new_sku(self): #funcion nos servira para guardar la data ingresada
		self.espera = [self.div.text,self.cat.text,self.subcat.text,self.med.text,self.marca.text , self.sku.text]
		
		if "" in self.espera:
			print("Datos Vacios o Incorrectos")
		else:			
			print(self.espera)
			print("Datos Correctos")
			self.search_results_list.item_strings = self.espera
class ReportesApp(App):
	title = 'reportes'
	icon = 'icon.png'
 
	def build(self):  
		return User()
	def on_pause(self):
		return True

if __name__ == '__main__':
	ReportesApp().run()
