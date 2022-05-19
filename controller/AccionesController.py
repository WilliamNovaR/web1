class Acciones:
    def __init__(self) -> None:
        super().__init__()
        self.acciones = ["Home", 'Crear cuenta', 'Iniciar sesion']
        self.iconos = [ 'house', 'person-plus', 'person-check' ]

    def agregar_evaluacion(self, evaluacion_obj):
        self.evaluaciones.append(evaluacion_obj)