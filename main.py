#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from  kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.listview import ListView
import time

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from tool  import fechas
import random
 	
"""
	POr investigar
	como usar los Popup para usarlo validar campos
	como ponemos visualizar en formade tabla los datos a imprimir y consultar
	buscar como hacer para enviar los datos  procesados
""" 
class Usuario(BoxLayout):
	def __init__(self, arg):
		super(Usuario, self).__init__(**kwargs)
		
class MaPopup(BoxLayout):
    cancel = ObjectProperty(None)
    # def __init__(self, **kwargs):
    #     kwargs['cols'] = 4
    #     super(MaPopup, self).__init__(**kwargs)

    #     list_view = ListView(item_strings=[str(index) for index in range(100)])

    #     self.add_widget(list_view)

class User(ScreenManager):
	nombre = ObjectProperty()
	empresa = ObjectProperty()
	calendario = fechas()

	estado = ObjectProperty()
	estado_ven = ObjectProperty()

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
	_popup = None

	def _dismiss_popup(self):
		self._popup.dismiss()
	def do_popup(self):
		# Instantiate MaPopup and give functionality to cancel butto
		
		#popup_content = MaPopup(cancel=self._dismiss_popup)
		popup_content =  ListView(item_strings=["{0}, {1}".format(clave,valor) for clave,valor in self.add.items()])
		self._popup = Popup(title = 'Bievenidos', size_hint = (0.5, 0.5), content=popup_content)
		self._popup.open()
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
		name = (self.nombre.text)
		empresa = (self.empresa.text)
		self.estado_ven.text="Menu Principal"
		if (name != "" and empresa != ""): self.estado.text="\t\tDatos Corrector ! \n\n\t\t\t\tBienvenido Nuevamente :)"; self.estado_ven.text ="Categoria"
		elif name == "" and empresa != "": self.estado.text="\t\tDatos Incorrecto!!!\n\n\t\t\t\t Falta Nombre"
		elif empresa == "" and name != "": self.estado.text="\t\tDatos Incorrecto!!!\n\n\t\t\t\tFalta Empresa"
		else: self.estado.text="\t\tDatos Incorrecto!!!\n\n\t\t\t\tFalta Ingresar: \n\n\t\t\t\t\t El Usuario y La Empresa"
		print("Usuario ----> "+self.estado.text, "ventana ----> "+self.estado_ven.text)

	def save_new_sku(self): #funcion nos servira para guardar la data ingresada
		#asignamos los valores temporablemente a una lista
		
		temp =[self.div.text,self.cat.text,self.subcat.text,self.med.text,self.marca.text , self.sku.text]
		
		self.espera = temp
		#agragamos a la lista los valores ingresados		
		if "" in self.espera:
			print("save_new_sku-- Datos Vacios o Incorrectos")
		else:
			self.espera =[]			
			for x in temp:
		 		self.espera.append(x)	

		 	self.sav = True		
			print(self.espera)
			print("save_new_sku-- Datos Correctos")
	def save(self): #funcion nos servira para guardar la data ingresada
		print(self.sav)

		# #self.espera =[]
		# temp =[(self.div.text).strip(),(self.cat.text).strip(),(self.subcat.text).strip(),(self.med.text).strip(),(self.marca.text ).strip(), (self.sku.text).strip()]
		# for x in temp:
		# 	self.espera.append(x)
		# if "" in self.espera:
		# 	print("save-- Datos Vacios o Incorrectos")
		# else:
		# 	#clave id  y los valores serial temp
						
		# 	print(self.add)
		# 	print("save-- Datos Correctos")
	def save_db(self,):
		print(self.sav)
		if self.sav == False:
			print("save_db-- No Procesados base da datos")
		else:	
			id = random.getrandbits(10)
			self.add[id]=self.espera
			self.resultado_lista.item_strings = ["{0}, {1}".format(clave,valor) for clave,valor in self.add.items()]
			print(self.add)
			print("save_db--Actualizar base da datos")
			self.sav = False
		print(self.sav)

class ReportesApp(App):
	title = 'reportes'
	icon = 'icon.png'
 
	def build(self):  
		return User()
	def on_pause(self):
		return True



if __name__ == '__main__':
	ReportesApp().run()
