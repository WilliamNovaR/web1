from model.Cuenta import Cuenta
import json

#esta funcion sirve para guardar las cuentas dentro de un .json
def cargar( cuentaController ):
    lista = []
    #se recorren todos los elementos dentro de cuentaController para guardarlo en un diccionario para poder guardarlo en el .json
    for i in cuentaController.cuentas:
        diccionario = {'usuario': '', 'contrasena': '', 'tipo': ''}
        diccionario['usuario'] = i.usuario
        diccionario['contrasena'] = i.contrasena
        diccionario['tipo'] = i.tipo
        lista.append(diccionario)
    #se abre y se guarda el diccionario en el .json
    with open('data_cuentas.json', 'w') as outfile:
        json.dump(lista, outfile)

#esta funcion sirve para poder crear cuentas de tipo asistente, jurado o director
def crear_cuenta(st, cuentaController):
    st.header( "Crear cuenta" )
    nueva_cuenta = Cuenta()
    #se leen los datos que va a tener la cuenta y se guardan dentro de nueva_cuenta
    nueva_cuenta.usuario = st.text_input( "Usuario:", value = '' )
    nueva_cuenta.contrasena = st.text_input( "Contraseña:", value= ''  )
    tipo = st.selectbox( "Que tipo de cuenta quieres crear?", ('Asistente', 'Jurado', 'Director/a') )
    crear = st.button( "Crear" )
    if crear:
        #comprueba que no se creen cuentas con usuarios ya creados
        for i in cuentaController.cuentas:
            if nueva_cuenta.usuario == i.usuario:
                st.error( "esta cuenta ya existe" )
                return
        #se guarda la cuenta dentro de cuentaController y se carga la cuenta en el .json
        nueva_cuenta.tipo = tipo
        cuentaController.cuentas.append( nueva_cuenta )
        cargar( cuentaController )
        st.success( "Cuenta creada" )

#funcion para iniciar sesiones creadas
def iniciar_sesion( st, cuentasController, accionesController):
    st.header("Iniciar sesion")
    #se leen los datos para iniciar sesion
    usuario = st.text_input( "Usuario:", key = 23 )
    contrasena = st.text_input( "Contraseña:", key = 7 )
    col1, col2 = st.columns([0.1,1])#se crean las columnas para pode tener los botonos de iniciar sesion y entrar juntos
    with col1:
        login = st.button( "Iniciar sesion" )
        if login:
            for i in cuentasController.cuentas:
                if usuario == i.usuario and contrasena == i.contrasena: #comprueba que el usuario y contraseña coicidan y esten creados
                    #los condicionales sirven para generar los menos diferente dependiendo del tipo de cuenta que se loguea
                    if i.tipo == 'Asistente':
                        accionesController.acciones = ['Home', 'Crear cuenta', 'Iniciar sesion', #este arreglo tiene las opciones de menu que se tendra si se inicia de cuenta asistente
                                                       'Inicilizar datos actas', 'Ver historico resumido actas',
                                                       'Estadisticas', 'Cerrar sesion']
                        accionesController.iconos = ['house', 'person-plus', 'person-check', 'upload', 'book', #en este arreglo se cargan los iconos que tendran cada uno de las opciones de menu
                                                     'file-bar-graph', 'person-x' ]
                    elif i.tipo == 'Jurado':
                        accionesController.acciones = ['Home', 'Crear cuenta', 'Iniciar sesion', 'Evaluar nuevo trabajo',
                                                       'Ver o editar calificaciones', 'Exportar acta' , 'Estadisticas', 'Cerrar sesion']
                        accionesController.iconos = ['house', 'person-plus', 'person-check', 'clipboard',
                                                     'clipboard-check', 'file-pdf','file-bar-graph', 'person-x']
                    elif i.tipo == 'Director/a':
                        accionesController.acciones = ['Home', 'Crear cuenta', 'Iniciar sesion',
                                                       'Modificar y ver criterios',
                                                       'Ver historico resumido actas', 'Estadisticas', 'Cerrar sesion']
                        accionesController.iconos = ['house', 'person-plus', 'person-check', 'list-check',
                                                     'book', 'file-bar-graph', 'person-x']
                    with col2:
                        st.button("Entrar")
                        return
            st.error( "Datos no validos" ) #en caso que la sesion no exista o no coicidan los datos muestra el error

#esta funcion es la que parmite salir de la sesion para poder volver a loguarse
def cerrar_sesion(st, accionesController):
    st.subheader( "Cerrar sesion" )
    col1, col2 = st.columns([0.1, 1]) #culumans para tener los botones de Cerrar sison y Salir juntos
    with col1:
        logout = st.button("Cerrar sesion")
        if logout:
            accionesController.acciones = ["Home", 'Crear cuenta', 'Iniciar sesion'] #se guardan las opciones de menu que se tienen cuando no se esta logueado
            accionesController.iconos = [ 'house', 'person-plus', 'person-check' ] #se guardan los iconos de estas opciones de menu
            with col2:
                st.button("Salir")







