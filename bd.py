# -*- coding: utf-8 *-*
from sqlalchemy import create_engine
import mysql.connector

from sqlalchemy  import exc
# resul = engine.execute( "SELECT * FROM test").fetchone()

class DML():
	"""DML"""
	def __init__(self,usuario='maryon',password='faru9510', host='localhost',nom_bd='faru'):
		'''inicializacion con parametros de configuracion BD'''
		self.usuario = usuario
		self.password= password 
		self.host= host
		self.nom_bd= nom_bd
		self.CrearConexion()

	def CrearConexion(self):
		''' Creacion de una conexion '''
		print("\n\t --CONECTANDONOS A LA BD MySQL-\n")
		engine= create_engine("mysql+mysqlconnector://{0}:{1}@{2}/{3}?host=localhost?port=3306".format(self.usuario,self.password,self.host,self.nom_bd))
		try:		
			self.bd = engine.raw_connection()	
			self.cursor = self.bd.cursor()
			estado=("\n!!!Conexion Exitosa!!!")
		except exc.ProgrammingError as err:
  			print("Something went wrong: {}".format(err))
  			estado=("\n!!!Error En la Conexion!!!")
		print(estado)
	def Mostrar(self, con):
		'''consulta Bd SELECT'''
		print("\n\t --CONSULTANDO EN LA BD--\n")
		# consulta = " SELECT * FROM data"
		consulta = "SELECT * FROM `data` WHERE `PRODUCT` LIKE '{}'".format(con)
		
		#fetchall Obtengo todos los valores Bd
		try:
			self.cursor.execute(consulta)
			self.resultados = self.cursor.fetchall()			
			if not self.resultados:
				estado= ("\n!!!Base De Datos vacia !!!")
				self.resultados =["No Hay Registro En la Base de Datos ...ADD..."]
				print (len(self.resultados))
			else:			
		   		# print("SKU \t DIVISION \t PRODUCT \t TYPE \t BRAND \t SIZE/CAPACITY")
		   		# for registro in self.resultados:
		   		# 	print("{0} \t {1} \t {2} \t {3} \t {4} \t {5}".format(str(registro[0]),str(registro[1]),str(registro[2]),str(registro[3]),str(registro[4]),str(registro[5])))
		   		estado=("\n!!!Consulta Exitosa!!!")
		   		print (len(self.resultados))
			self.cursor.close()
		except:
			self.resultados =[]
			estado=("\n!!!Erro: No se pudo obtener los datos!!!")
		print(estado)
		return self.resultados
# objeto = DML()
# objeto.Mostrar("DA")
	# def Insertar(self):
	# 	'''Insertar datos en la BD INSERT'''
	# 	print("\n\t --AGREGANDO DATOS A LA BD--\n")
	# 	try:
	# 		cedula =input("Ingrese su Cedula:")
	# 		nombre =input("Ingrese su nombre:")
	# 		edad =int(input("Ingrese su edad:"))
	# 		Insertar = ("INSERT INTO test (nombre, cedula, edad) VALUES ('%s','%s','%i')"%(nombre,cedula,edad))
	# 		self.cursor.execute(Insertar)
	# 		self.bd.commit()

	# 		estado=("\n!!!Datos Insertar Exitosamente!!!")
	# 	except mysql.connector.Error as err:
	# 		estado=("\n!!!Erro al Insertar Datos!!!",err)
	# 	print(estado)

	# def Actualizar(self):
	# 	'''Actualizar datos en la BD UPDATE'''
	# 	print("\n\t --ACTUALIZANDO LA BD--\n")
	# 	try:
	# 		cedula =input("Ingrese su Cedula Actual:")
	# 		nueva_cedula=input("Ingrese su La Nueva Cedula:")
	# 		consulta_actualizar = ("SELECT * FROM test WHERE cedula LIKE '%s'"%(cedula))
	# 		status=self.verificacion(consulta_actualizar)
	# 		if status == None:
	# 			estado= ("\n!!!Dato No Encontrado en la BD!!!")
	# 		else:
	# 			actualizar=("UPDATE test SET cedula='%s' WHERE cedula='%s' "%(nueva_cedula,cedula))
	# 			self.cursor.execute(actualizar)
	# 			self.bd.commit()

	# 			estado=("\n!!!Datos Actulizados Exitosamente!!!")
	# 	except mysql.connector.Error as err:
	# 		estado=("\n!!!Erro al Actualizar Datos!!!",err)
	# 	print(estado)
	# def Eliminar(self):
	# 	'''Eliminar registros en la BD DELETE'''
	# 	print("\n\t --ELIMINANDO DATOS EN LA BD--\n")
	# 	try:
	# 		criterio = input("Ingrese nombre que desea eliminar: ")
	# 		# hacemos una consulta para saber si el dato ingresado esta en la tabla
	# 		consulta_eliminar = ("SELECT * FROM test WHERE nombre LIKE '%s'"%(criterio))
	# 		status=self.verificacion(consulta_eliminar)
	# 		if status == None:
	# 		   	estado= ("\n!!!Dato No Encontrado en la BD!!!")
	# 		else:			
	# 			self.cursor = self.bd.cursor()
	# 			criterio_consulta = ("DELETE FROM test WHERE nombre = '%s'" % (criterio ))
	# 			self.cursor.execute(criterio_consulta)
	# 			self.bd.commit()

	# 			estado=("\n!!!Datos Eliminado Exitosamente!!!")
	# 	except mysql.connector.Error as err:
	# 		estado=("\n!!!Error al Eliminar Datos !!!",err)
	# 	print(estado)
	
	# def verificacion(self,consulta):
	# 	self.cursor = self.bd.cursor()
	# 	self.cursor.execute(consulta)
	# 	status = self.cursor.fetchone()
	# 	return(status)
	# def Cerrar_Conexion(self):
	# 	self.cursor.close()
	# 	self.bd.close()
	# 	print("\n!!!Conexion Cerradas!!!\n".center(90, "*"))

