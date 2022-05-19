from model.Acta import PDF
from datetime import datetime
import base64
import json

#esta funcion sirve para cargar en un .json las actas y guardarlas para que no se borren cada vez que se ejecuta el programa

def cargar( actas_controller ):
    lista = []
    #convierte las actas en diccionarios para poder guardalas dentro de un .json
    for i in actas_controller.actas:
        diccionario = {'fuente': '', 'inicializar': '', 'nombre_pdf': '', 'fecha': '', 'num_acta': '', 'titulo': '', 'autor': '', 'id': '', 'periodo': '', 'director': '', 'codirector': '', 'enfasis': '', 'modalidad': '', 'jurado1': '', 'jurado2': '', 'num_criterio': '', 'nombre_criterio': '', 'ponderacion': '', 'calificacion': '', 'observacion': '', 'calificacion_final': '', 'unidad': '', 'decima': '', 'comentario_final': '', 'correcciones': '', 'recomendacion': '' }
        diccionario['fuente'] = i.fuente
        diccionario['inicializar'] = i.inicializar
        diccionario['nombre_pdf'] = i.nombre_pdf
        diccionario['fecha'] = i.fecha
        diccionario['num_acta'] = i.num_acta
        diccionario['titulo'] = i.titulo
        diccionario['autor'] = i.autor
        diccionario['id'] = i.id
        diccionario['periodo'] = i.periodo
        diccionario['director'] = i.director
        diccionario['codirector'] = i.codirector
        diccionario['enfasis'] = i.enfasis
        diccionario['modalidad'] = i.modalidad
        diccionario['jurado1'] = i.jurado1
        diccionario['jurado2'] = i.jurado2
        diccionario['num_criterio'] = i.num_criterio
        diccionario['nombre_criterio'] = i.nombre_criterio
        diccionario['ponderacion'] = i.ponderacion
        diccionario['calificacion'] = i.calificacion
        diccionario['observacion'] = i.observacion
        diccionario['calificacion_final'] = i.calificacion_final
        diccionario['unidad'] = i.unidad
        diccionario['decima'] = i.decima
        diccionario['comentario_final'] = i.comentario_final
        diccionario['correcciones'] = i.correcciones
        diccionario['recomendacion'] = i.recomendacion
        lista.append(diccionario)
    #carga la informacion dentro del .json
    with open('data_actas.json', 'w') as outfile:
        json.dump(lista, outfile)


# esta funcion permite crear la opcion de descargar la acta creada
def create_download_link(val, filename):
    b64 = base64.b64encode(val) #Codifica el objeto similar a bytes s utilizando Base64 y retorna los bytes codificados
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

#la funcion establece los datos del acta y permite descargarla
def crearActa(st, actas_controller, controller):
    st.title("Crear acta")
    lista_nombres = [] # creamos un arreglo para almacenar todos los nombres de los estudiantes calificados para poner estos en el select box
    fuente = 'Helvetica'
    for nombres in controller.evaluaciones:
        if len(nombres.calificacion) > 0 :
            lista_nombres.append(nombres.nombre_autor) #el ciclo recorre el arreglo que tiene todas las calificaciones y guarda en el arreglo los nombres calificados
    seleccionar_estudiante_acta = st.selectbox("a que estudiante le quieres hacer el acta?", lista_nombres)
    if len( lista_nombres ) < 1:
        st.error( "No se ha calificado a ningun estudiante" )
    indice_estudiante = 0 #esta variable nos sirve para saber el indice del estudiante en el arreglo de la clase Evalcontroller
    key = 7 #esta key nos permite imprimir repetodos st.inputs mediante un for ya que si no nos da error
    #encuentra al estudiante al cual se le va a generar el acta
    for nombre in controller.evaluaciones:
        if nombre.nombre_autor == seleccionar_estudiante_acta:
            acta = PDF('P', 'mm', 'Letter') #inicializa datos del pdf como la horientacion y el tamaño
            acta.fuente = fuente
            acta.nombre_pdf = 'acta' + str(len(actas_controller.actas) + 1) + seleccionar_estudiante_acta + '.pdf'
            acta.nombre_pdf = st.text_input("Nombre con el que se guardara el pdf del acta", value=acta.nombre_pdf, key = key) #pregunta el nombre con el que se va a generar el archivo del acta
            if st.button("Crear acta", key = key * 123):
                acta.set_left_margin(10.0) #setea las margenes
                acta.fecha = datetime.today().strftime('%Y-%m-%d') #optiene la fecha
                acta.num_acta = str(len(actas_controller.actas) + 1) + '-' + datetime.today().strftime('%Y') #crea el numero del acta
                acta.set_auto_page_break(auto=True, margin=15) #Habilita o deshabilita el modo de salto de página automático el segundo parámetro es la distancia desde la parte inferior de la página
                acta.add_page() #inicializa otra pagina
                #estable los datos del acta
                acta.titulo += controller.evaluaciones[indice_estudiante].nombre_trabajo + '"'
                acta.autor = controller.evaluaciones[indice_estudiante].nombre_autor
                acta.id = controller.evaluaciones[indice_estudiante].id_estudiante
                acta.periodo = controller.evaluaciones[indice_estudiante].periodo
                acta.director = controller.evaluaciones[indice_estudiante].nombre_director
                acta.codirector = controller.evaluaciones[indice_estudiante].nombre_codirector
                acta.enfasis = controller.evaluaciones[indice_estudiante].enfasis
                acta.modalidad = controller.evaluaciones[indice_estudiante].tipo_trabajo
                acta.jurado1 = controller.evaluaciones[indice_estudiante].nombre_jurado1
                acta.jurado2 = controller.evaluaciones[indice_estudiante].nombre_jurado2
                acta.datos() #imprime los datos con los que se inicializa el acta
                contador = 1 # sirve para darle un numero a la viñeta de cada criterio
                for i in controller.evaluaciones[indice_estudiante].calificacion:
                    #imprime los datos de los criterios y sus calificaciones y observaciones
                    acta.num_criterio = str(contador) + "."
                    acta.nombre_criterio = i.id_criterio
                    acta.ponderacion = 'Ponderacion: ' + str(i.ponderacion * 100) + '%'
                    acta.calificacion = str(i.nota_final)
                    acta.observacion = 'Observaciones: ' + i.comentario
                    acta.criterio()
                    contador += 1
                #imprime nota final del trabajo, comentario final y correciones
                acta.calificacion_final = str(controller.evaluaciones[indice_estudiante].nota)
                acta.comentario_final = 'Observaciones adicionales: ' + controller.evaluaciones[indice_estudiante].comentario_final
                acta.correcciones = 'La calificación final queda sujeta a que se implementen las siguientes correcciones: ' + controller.evaluaciones[indice_estudiante].correciones
                acta.nota_final()
                acta.firmas()
                #verifica si la nota del estudiante es suficiente para una condecoracion
                if float(acta.calificacion_final) >= 4.5:
                    acta.add_page()
                    acta.datos()
                    acta.extra()
                #da la opcion de imprimir y guardar el acta en ActaController
                html = create_download_link(acta.output(dest="S").encode("latin-1"), acta.nombre_pdf)
                actas_controller.actas.append(acta)
                st.markdown(html, unsafe_allow_html=True)
                cargar( actas_controller )
                st.success("Acta Creada")
            key *= key + 4 #cambia la key para no generar errores
        indice_estudiante += 1
