from model.Criterio import Criterio
import json

#esta funcion sirve para cargar en un .json los criterios y guardarlas para que no se borren cada vez que se ejecuta el programa

def cargar( criterios_controller ):
    lista = []
    #convierte en un diccionario los criterios para poderlos cargar en el .json
    for i in criterios_controller.criterios:
        diccionario = {'identificador': '', 'descripcion': '', 'porcentaje_ponderacion': ''}
        diccionario['identificador'] = i.identificador
        diccionario['descripcion'] = i.descripcion
        diccionario['porcentaje_ponderacion'] = i.porcentaje_ponderacion
        lista.append(diccionario)
    # carga la informacion dentro del .json
    with open('data_criterios.json', 'w') as outfile:
        json.dump(lista, outfile)

#funcion que crea el selector de opciones
def seleccionar_opcion(st, criterios_controller):
    st.title("Criterios")
    opcion = st.radio("Tipo de trabajo", ('Listar', 'Agregar', 'Editar', 'Eliminar'))
    if opcion == 'Listar':
        listar_criterio(st, criterios_controller)
    elif opcion == 'Agregar':
        agregar_criterio(st, criterios_controller)
    elif opcion == 'Editar':
        editar_criterio(st, criterios_controller)
    elif opcion == 'Eliminar':
        eliminar_criterio(st, criterios_controller)

#imprime todos los criterios y sus descripciones
def listar_criterio(st, criterios_controller):
    st.subheader("Lista de criterios")
    for criterio in criterios_controller.criterios:
        st.subheader("Nombre: " + criterio.identificador)
        st.write("Porcentaje ponderacion: " + str(criterio.porcentaje_ponderacion))
        st.write("Descripcion: " + criterio.descripcion)

#funcion para agregar criterios
def agregar_criterio(st, criterios_controller):
    st.subheader("Agregar criterio")
    criterio = Criterio("", "", 0) #crea un nuevo objeto criterio el cual sera al que le carguemos los datos y agreguemos
    #lee datos
    criterio.identificador = st.text_input(" Digite el identificador del criterio ")
    criterio.descripcion = st.text_input(" Digite una descripcion para el criterio")
    criterio.porcentaje_ponderacion = st.number_input('agregue el porcentaje ponderado del criterio')
    if st.button("Enviar"):
        #guarda los datos y carga en el .json
        criterios_controller.agregar_criterios(criterio)
        st.success("Tarea exitosa")
        cargar( criterios_controller )
    return criterios_controller

#funcion para cambiar los valores de evaluacion de los criterios ####!!!! hacer ecepciones aqui
def editar_criterio(st, criterios_controller):
    #carga el valor mayor y menor de ponderacion que puede tener un criterio
    menor_valor = 0
    maximo_valor = 1
    st.subheader("Editar criterio")
    lista_criterios = []
    #guarda los nombres de los criterios en el arreglo lista_criterios para que salga en la select box
    for i in criterios_controller.criterios:
        lista_criterios.append(i.identificador)
    seleccionar_criterio = st.selectbox("Escoger criterio", lista_criterios)
    #busca el criterio seleccionado e imprime y lee sus valores
    for criterios in criterios_controller.criterios:
        contador = 1
        if seleccionar_criterio == criterios.identificador:
            criterios.identificador = st.text_input(" Digite el identificador del criterio ",
                                                    value=criterios.identificador)
            criterios.descripcion = st.text_input(" Digite una descripcion para el criterio",
                                                  value=criterios.descripcion)
            criterios.porcentaje_ponderacion = st.number_input('agregue el porcentaje ponderado del criterio',
                                                               value=criterios.porcentaje_ponderacion )
            contador +=1
            if st.button("Editar"):
                cargar(criterios_controller)
                st.success("Edicion exitosa")

#Elimina el criterio seleccionado
def eliminar_criterio(st, criterios_controller):
    lista_criterios = []
    index = 0 #en esta variable se guarda el index del criterio que vamos a eliminar
    # guarda los nombres de los criterios en el arreglo lista_criterios para que salga en la select box
    for i in criterios_controller.criterios:
        lista_criterios.append(i.identificador)
    seleccionar_criterio = st.selectbox("Escoger criterio", lista_criterios)
    # busca el criterio seleccionado e imprime sus valores
    for criterios in criterios_controller.criterios:
        #busca el criterio que se quiere eliminar
        if seleccionar_criterio == criterios.identificador:
            st.write( "Quieres eliminar el criterio " + seleccionar_criterio + "?" )
            eliminar = st.button( "Eliminar" )
            if eliminar:
                criterios_controller.criterios.pop( index )#elimina el criterio
                cargar(criterios_controller)
                st.success( "Elemento Eliminado" )
                #se elimana criterios y se carga en .json el cambio
        index += 1

