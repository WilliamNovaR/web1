import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from controller.memoria import Data
from controller.AccionesController import Acciones
from controller.CuentaController import Cuentas
from controller.EvalController import EvaluadorController
from controller.CriterioController import CriterioController
from controller.ActaController import ActaController
from model.Cuenta import Cuenta
from model.Criterio import Criterio
from model.Acta import PDF
from model.Calificacion import Calificacion
from model.EvalEstudiante import EvaluacionEstudiante
from view.Home import consultar_instrucciones
from view.sesion import crear_cuenta, iniciar_sesion, cerrar_sesion
from view.Evaluar import seleccion, agregar_evaluacion
from view.ConfigurarCriterios import seleccionar_opcion
from view.CrearActa import crearActa
from view.InicializarActa import agregar_datos
from view.InformacionActas import listar_actas
from view.AnaliticaDatos import escoger_analis
import json
import os.path





class MainView:
    def __init__(self) -> None:
        super().__init__()

        # Estretagia para manejar el "estado" del controllador y del modelo entre cada cambio de ventana
        if 'main_view' not in st.session_state:
            self.menu_actual = "About"

            # Conexión con el controlador
            self.data = Data()
            self.acciones = Acciones()
            self.cuentas_controller = Cuentas()
            self.controller = EvaluadorController()
            self.criterios_controller = CriterioController()
            self.actas_controller = ActaController()

            st.session_state['main_view'] = self
        else:
            # Al exisir en la sesión entonces se actualizan los valores
            self.data = st.session_state.main_view.data
            self.acciones = st.session_state.main_view.acciones
            self.menu_actual = st.session_state.main_view.menu_actual
            self.cuentas_controller = st.session_state.main_view.cuentas_controller
            self.controller = st.session_state.main_view.controller
            self.criterios_controller = st.session_state.main_view.criterios_controller
            self.actas_controller = st.session_state.main_view.actas_controller
        self._dibujar_layout()
        #comprueba que los archivos esten creados para cargar los datos guardados en los .json y asi no se pierda la info
        if os.path.exists( 'data_cuentas.json' ):
            with open('data_cuentas.json') as json_file:
                data = json.load(json_file)
                lista = []
                for crear in data:
                    cargar_cuenta = Cuenta()
                    cargar_cuenta.usuario = crear['usuario']
                    cargar_cuenta.contrasena = crear[ 'contrasena' ]
                    cargar_cuenta.tipo = crear[ 'tipo' ]
                    lista.append( cargar_cuenta )
            self.cuentas_controller.cuentas = lista
        if os.path.exists( 'data_criterios.json' ):
            with open('data_criterios.json') as json_file:
                data = json.load(json_file)
                lista = []
                for crear in data:
                    cargar_cuenta = Criterio( crear['identificador'], crear[ 'descripcion' ], crear[ 'porcentaje_ponderacion' ] )
                    lista.append( cargar_cuenta )
            self.criterios_controller.criterios = lista
        if os.path.exists( 'data_actas.json' ):
            with open('data_actas.json') as json_file:
                data = json.load(json_file)
                lista = []
                for crear in data:
                    cargar_acta = PDF('P', 'mm', 'Letter')
                    cargar_acta.fuente = crear['fuente']
                    cargar_acta.inicializar = crear['inicializar']
                    cargar_acta.nombre_pdf = crear['nombre_pdf']
                    cargar_acta.fecha = crear['fecha']
                    cargar_acta.num_acta = crear['num_acta']
                    cargar_acta.titulo = crear['titulo']
                    cargar_acta.autor = crear['autor']
                    cargar_acta.id = crear['id']
                    cargar_acta.periodo = crear['periodo']
                    cargar_acta.director = crear['director']
                    cargar_acta.codirector = crear['codirector']
                    cargar_acta.enfasis = crear['enfasis']
                    cargar_acta.modalidad = crear['modalidad']
                    cargar_acta.jurado1 = crear['jurado1']
                    cargar_acta.jurado2 = crear['jurado2']
                    cargar_acta.num_criterio = crear['num_criterio']
                    cargar_acta.nombre_criterio = crear['nombre_criterio']
                    cargar_acta.ponderacion = crear['ponderacion']
                    cargar_acta.calificacion = crear['calificacion']
                    cargar_acta.observacion = crear['observacion']
                    cargar_acta.calificacion_final = crear['calificacion_final']
                    cargar_acta.unidad = crear['unidad']
                    cargar_acta.decima = crear['decima']
                    cargar_acta.comentario_final = crear['comentario_final']
                    cargar_acta.correcciones = crear['correcciones']
                    cargar_acta.recomendacion = crear['recomendacion']
                    lista.append( cargar_acta )
            self.actas_controller.actas = lista
        if os.path.exists( 'data_calificaciones.json' ):
            with open('data_calificaciones.json') as json_file:
                data = json.load(json_file)
                arreglo = []
                for cargar in data:
                    lista = []
                    evaluaciones = EvaluacionEstudiante()
                    for datos in cargar['calificacion']:
                        calificacion = Calificacion()
                        calificacion.numero_jurados = datos['numero_jurados']
                        calificacion.id_criterio = datos['id_criterio']
                        calificacion.ponderacion = datos['ponderacion']
                        calificacion.nota_jurado1 = datos['nota_jurado1']
                        calificacion.nota_jurado2 = datos['nota_jurado2']
                        calificacion.nota_final = datos['nota_final']
                        calificacion.comentario = datos['comentario']
                        lista.append(calificacion)
                    evaluaciones.calificacion = lista
                    evaluaciones.id_estudiante = cargar['id_estudiante']
                    evaluaciones.periodo = cargar['periodo']
                    evaluaciones.nombre_autor = cargar['nombre_autor']
                    evaluaciones.nombre_trabajo = cargar['nombre_trabajo']
                    evaluaciones.tipo_trabajo = cargar['tipo_trabajo']
                    evaluaciones.nombre_director = cargar['nombre_director']
                    evaluaciones.nombre_codirector = cargar['nombre_codirector']
                    evaluaciones.enfasis = cargar['enfasis']
                    evaluaciones.nombre_jurado1 = cargar['nombre_jurado1']
                    evaluaciones.nombre_jurado2 = cargar['nombre_jurado2']
                    evaluaciones.inicilizar = cargar['inicilizar']
                    evaluaciones.nota = cargar['nota']
                    evaluaciones.comentario_final = cargar['comentario_final']
                    evaluaciones.correciones = cargar['correciones']
                    evaluaciones.recomendacion = cargar['recomendacion']
                    arreglo.append(evaluaciones)
                self.controller.evaluaciones = arreglo




    def _dibujar_layout(self):
        img = Image.open("puj_logo_vertical_azul_copia.png") #carla la imagen del icono de la pagina
        # Set page title, icon, layout wide (more used space in central area) and sidebar initial state
        st.set_page_config(page_title="Calificar trabajos finales", page_icon=img, layout="wide",
                            initial_sidebar_state="expanded")

        self.no_errores = 1
        # Defines the number of available columns del area principal
        self.col1, self.col2, self.col3, self.col4, self.col5, self.col6, self.col7, self.col8 = st.columns(
            [1, 1, 1, 1, 1, 1, 1, 1])

        # Define lo que abrá en la barra de menu
        with st.sidebar:
            self.menu_actual = option_menu("Menu",
                                        self.acciones.acciones,
                                        icons= self.acciones.iconos, menu_icon="cast",
                                        default_index=0)

    def controlar_menu(self):
        if self.menu_actual == "Home":
            consultar_instrucciones( st )
        elif self.menu_actual == 'Crear cuenta':
            crear_cuenta( st, self.cuentas_controller )
        elif self.menu_actual == 'Iniciar sesion':
            iniciar_sesion( st, self.cuentas_controller, self.acciones )
        elif self.menu_actual == "Inicilizar datos actas":
            agregar_datos(st, self.controller)
        elif self.menu_actual == "Modificar y ver criterios":
            seleccionar_opcion(st, self.criterios_controller)
        elif self.menu_actual == "Evaluar nuevo trabajo":
            agregar_evaluacion(st, self.controller, self.criterios_controller)
        elif self.menu_actual == "Ver o editar calificaciones":
            seleccion(st, self.controller, self.criterios_controller)
        elif self.menu_actual == "Exportar acta":
            crearActa(st, self.actas_controller, self.controller)
        elif self.menu_actual == "Ver historico resumido actas":
            listar_actas(st, self.criterios_controller, self.actas_controller)
        elif self.menu_actual == 'Estadisticas':
            escoger_analis(st, self.controller, self.criterios_controller)
        elif self.menu_actual == 'Cerrar sesion':
            cerrar_sesion(st, self.acciones)


# Main call

if __name__ == "__main__":
    main = MainView()
    main.controlar_menu()
