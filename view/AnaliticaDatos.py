from model.EvalEstudiante import EvaluacionEstudiante
import matplotlib.pyplot as plt

#en este documento se la funcion para la anaticia de datos

def escoger_analis(st, controller, criterio_controler):
    notas = []
    nombres = []
    opcion = st.radio("Que analisis quieres hacer?",
                  ('Encontrar Calificacion más alta', 'Estadisticas notas', 'Estadistica criterios'))
    if opcion == 'Encontrar Calificacion más alta':
        mayor_calificacion( st, controller )
    elif opcion == 'Estadisticas notas':
        grafica_notas( st, controller, notas, nombres )
    elif opcion == 'Estadistica criterios':
        grifica_criterios(st, controller, criterio_controler, notas, nombres)

#esta funcion busca al estudiante con mayor nota e imprime los datos
def mayor_calificacion(st, controller):
    #primero se revisa que se hayan calificado estudiantes de lo contrario hay mensaje de error
    if len(controller.evaluaciones) > 0:
        mejor_calificacion = EvaluacionEstudiante()
        #recorre todos los estudiantes calificados para buscar el que tenga mayor nota final
        for i in controller.evaluaciones:
            if i.nota > mejor_calificacion.nota:
                mejor_calificacion = i
        #imprime los tados
        st.subheader("El estudiante con mejor calificiacion es: " + mejor_calificacion.nombre_autor)
        st.subheader("Id:" + mejor_calificacion.id_estudiante)
        st.subheader("Trabajo:" + mejor_calificacion.nombre_trabajo)
        st.subheader("Nota: " + str(round(mejor_calificacion.nota, 1)))
    else:
        st.error("No han calificado a nadie")

#esta funcion grafica las notas finales de todos los estudiantes calificados
def grafica_notas( st, controller, notas, nombres ):
    for i in controller.evaluaciones:
        #revisa que los nombres que se van a agregar a la grafica ya esten calificados y no solo inicilizados
        if len(i.calificacion) > 0:
            nombres.append(i.nombre_autor)
            notas.append(i.nota)
    #establece las dimenciones de la grafica
    fig = plt.figure(figsize=(10, 5))
    #se establece que datos va a ser el eje x y el y
    plt.bar(nombres, notas)
    #le da un titulo que describe a los datos de x y y
    plt.xlabel("Notas de estudiantes")
    plt.ylabel("Nombre estudiantes")
    plt.title("Notas")
    #imprime tabla
    st.pyplot(fig)


def grifica_criterios( st, controller, criterio_controler, notas, nombres ):
    #crea una grafica con la nota promedio de todos los criterios
    cantidad = 0
    numeros_criterio = []
    contador = 1
    #cuenta el numero de estudiates calificados
    for personas in controller.evaluaciones:
        if len(personas.calificacion) > 0:
            cantidad += 1
    for name in criterio_controler.criterios:
        notas.append(0) #crea los espacios en el arreglo para guardar el promedio de notas
        nombres.append(name.identificador) #agrega los nombres de los criterios a un arreglo
        numeros_criterio.append(contador) #establece un numero para cada criterio
        contador += 1 #variable encargada de dar un numero a cada criterio
    # recorre cada una de las calificaciones y realiza la sumatoria de la nota de cada criterio por estudiante
    for i in controller.evaluaciones:
        for j in range(len(i.calificacion)):
            notas[j] += i.calificacion[j].nota_final
    #saca el promedio de las notas
    for k in range(len(notas)):
        if cantidad > 0:
            notas[k] /= cantidad
    #crea e imprime tabla
    fig = plt.figure(figsize=(10, 5))
    plt.bar(numeros_criterio, notas)
    plt.xlabel("Criterios")
    plt.ylabel("Notas criterios")
    plt.title("Notas")
    st.pyplot(fig)
    for iterador in range(len(nombres)):
        st.write(str(numeros_criterio[iterador]) + " = " + nombres[iterador])
