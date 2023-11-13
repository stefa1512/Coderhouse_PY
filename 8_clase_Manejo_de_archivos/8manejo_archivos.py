# 1. Abrir el archivo (obligatorio)
#   a. ruta donde se encuentra el archivo
#   b. que permisos voy a brindar al archivo, a-> adicion al archivo
                                             #w-> sobreescritura
                                             #r-> sobreescritura
                                             #rb-> sobreescritura
# 2. Escribir/leer archivo
#.3. Cerrar archivo (obligatorio)

#sobreescritura
# fil = open("prueba1.txt","w")
# fil.write("Hola desde Coder")
# fil.close()

#escritura
#fil = open("prueba1.csv","a")
#fil.write("Hola desde Coder")
#fil.close()

#lectura
#read - lectura completa
# readline - lectura de un sola línea
# readlines - iterable con lectura de todas las líneas
#with open("prueba1.csv") as f:
#     #print(f.read())
#     #print(f.readline())
#     i = 0
#     for line in f.readlines():
#         print(line)
#         i += 1
#         if i == 2:
#             print("esta es la linea 2")

# import json
# user_dic = {
#     "estudiantes": [
#         {
#             "nombre": "luis",
#             "edad": 34
#         },
#         {
#             "nombre": "Rodrigo",
#             "edad": 26
#         },
#         {
#             "nombre": "Maria",
#             "edad": (42,34)
#         },
#     ]
# }
# # user_str = json.dumps(user_dic, indent=2) # de dict a str
# # with open("estudiantes.txt","w") as fil:
# #     fil.write(user_str)


# with open("estudiantes.txt","r") as fil:
#       estudiantes_str = fil.read()
#
# estudiantes_dic = json.loads(estudiantes_str) # se pasa el loads de str a dic
# print("El nombre del estudiante es: "+estudiantes_dic["estudiantes"][1]["nombre"])
# print(estudiantes_dic["estudiantes"][1]["edad"])


# with open("senderos_escolares_2023.csv") as fil:
#     i = 0
#     for line in fil.read():
#         print(line)
#         i += 1
#         if i == 10:
#             break

import pandas
datos = pandas.read_csv("resultados-del-test.csv")
print(datos.edad.head(5))
pass
