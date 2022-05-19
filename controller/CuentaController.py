class Cuentas:
    def __init__(self) -> None:
        super().__init__()
        self.cuentas = []

    def agregar_evaluacion(self, acta_obj):
        self.cuentas.append(acta_obj)