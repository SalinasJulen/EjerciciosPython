estudiantes = [
    {'nombre' : 'Paco', 'edad' : 23, 'registrado' : False, 'nota_entrada' : 85},
    {'nombre' : 'Julen', 'edad' : 18, 'registrado' : True, 'nota_entrada' : 90},
    {'nombre' : 'Marcelo', 'edad' : 55, 'registrado' : True, 'nota_entrada' : 60},
    {'nombre' : 'María', 'edad' : 17, 'registrado' : True, 'nota_entrada' : 75}
]


aceptada_o_no = True

for estudiante in estudiantes:
    if estudiante['edad'] >= 18 and estudiante['registrado'] == True and estudiante['nota_entrada'] >= 70:
        print(estudiante['nombre'] + " Solicitud aceptada")
    elif estudiante['edad'] < 18:
        print(estudiante['nombre'] + " Solicitud denegada por ser menor")
        aceptada_o_no = False
    elif estudiante['registrado'] != True:
        print(estudiante['nombre'] + " Solicitud denegada por no estar registrado")
        aceptada_o_no = False
    elif estudiante['nota_entrada'] < 70:
        print(estudiante['nombre'] + " Solicitud denegada por no tener la nota de entrada necesaria")
        aceptada_o_no = False

print("\n")

for x in estudiantes:
    print(x['nombre'] + " Solicitud aceptada") if x['edad'] >= 18 and x['registrado'] == True and x['nota_entrada'] >= 70  else print(x['nombre'] + " Solicitud denegada")
