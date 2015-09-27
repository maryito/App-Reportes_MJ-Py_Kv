#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from  kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager,Screen
import time
from kivy.uix.label import Label
from tool  import fechas


class User(ScreenManager):
	nombre = ObjectProperty()
	empresa = ObjectProperty()
	calendario = fechas()
	def horario(self):
		self.fecha= self.calendario[0]
		self.hora= self.calendario[1]

	def usuario(self):
		name = (self.nombre.text).strip()
		empresa = (self.empresa.text).strip()

		if name != "" and name != "":
			print("Bien")
			# self.status =""
			# print("Usuario: "+name, "Ventana: "+self.status)
		else:
			print("Falta")
			# self.status = "usu"
			# print("Usuario: "+name, "Ventana: "+self.status)

		
class ReportesApp(App):
	title = 'reportes'
	icon = 'icon.png'
 
	def build(self):  
		return User()
	def on_pause(self):
		return True

if __name__ == '__main__':
	ReportesApp().run()
