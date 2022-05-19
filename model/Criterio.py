
#clase creada para generar los criterios de evaluacion

class Criterio:
    #constructores
    def __int__(self) -> None:
        self.identificador = ""
        self.descripcion = ""
        self.porcentaje_ponderacion = None

    def __init__(self, identificador, descripcion, porcentaje_ponderacion):
        self.identificador = identificador
        self.descripcion = descripcion
        self.porcentaje_ponderacion = porcentaje_ponderacion