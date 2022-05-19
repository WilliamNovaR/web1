class EvaluadorController:
    def __init__(self) -> None:
        super().__init__()
        self.evaluaciones = []

    def agregar_evaluacion(self, evaluacion_obj):
        self.evaluaciones.append(evaluacion_obj)