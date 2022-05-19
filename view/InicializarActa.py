from model.EvalEstudiante import EvaluacionEstudiante
from view.Evaluar import cargar
from datetime import datetime




#inicializa la acta
def agregar_datos(st, controller):
    limite_semestre = 7
    mes = int(datetime.today().strftime('%m')) #optiene el mes para saber en que semestre estamos
    st.title("Calificar Trabajos")
    evaluacion_obj = EvaluacionEstudiante()
    evaluacion_obj.id_estudiante = st.text_input("Id estudiante")
    #si el mes es inferior a 7 toma como si fuera el semestre 1 en otro caso lo toma como semestre 2 esto es importante para la acta
    if mes < limite_semestre:
        evaluacion_obj.periodo = datetime.today().strftime('%Y') + '-' + '1: '
    else:
        evaluacion_obj.periodo = datetime.today().strftime('%Y') + '-' + '2: '
    #lee datos de inicializacion de acta
    evaluacion_obj.periodo = st.text_input("Periodo de evaluacion", value=evaluacion_obj.periodo)
    evaluacion_obj.nombre_autor = st.text_input("Nombre del autor", value =evaluacion_obj.nombre_autor )
    evaluacion_obj.tipo_trabajo  = st.selectbox("Tipo de trabajo", ('Aplicado', 'Investigacion'))
    evaluacion_obj.nombre_trabajo = st.text_input("Nombre del trabajo", value=evaluacion_obj.nombre_trabajo )
    evaluacion_obj.nombre_director = st.text_input("Nombre del director",value= evaluacion_obj.nombre_director )
    codirector = st.selectbox( "El trabajo tiene coodirector?", ('Si', 'No') )
    if codirector == 'Si':
        evaluacion_obj.nombre_codirector = st.text_input( "Nombre codirector: " )
    evaluacion_obj.enfasis = st.text_input("Enfasis en:", value= evaluacion_obj.enfasis)
    evaluacion_obj.nombre_jurado1 = st.text_input("Nombre del jurado1", value=evaluacion_obj.nombre_jurado1 )
    evaluacion_obj.nombre_jurado2 = st.text_input("Nombre del jurado2", value= evaluacion_obj.nombre_jurado2 )
    #pregunta el numero del acta desde el cual se va a empezar
    if len(controller.evaluaciones):
        evaluacion_obj.inicilizar = st.number_input("Numero de acta:", value=controller.evaluaciones[
                                                                                 len(controller.evaluaciones) - 1].inicilizar + 1,
                                                    step=1)#se sugiere el numero siguiente al de la anterior calificacion
    else:
        evaluacion_obj.inicilizar = st.number_input("Numero de acta:", step=1) #en caso de no haber calificaciones anteriores no se sugiere nada
    enviado_btn = st.button("Send")

    if enviado_btn:
        #con este for se comprueba que no hayan dos actas inicializadas con el mismo id en caso que si muestra el error y termina la funcion
        for i in controller.evaluaciones:
            if evaluacion_obj.id_estudiante == i.id_estudiante:
                st.error( "Id repetida" )
                return
        controller.evaluaciones.append( evaluacion_obj )
        cargar( controller )
        st.success("Evaluacion agregada exitosamente")
    else:
        st.error("Faltan criterios por calificar!")

    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller
