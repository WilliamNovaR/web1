class ActaController:
    def __init__(self) -> None:
        super().__init__()
        self.actas = []

    def agregar_evaluacion(self, acta_obj):
        self.actas.append(acta_obj)