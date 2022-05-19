from model.Criterio import Criterio



class CriterioController:
    def __init__(self) -> None:
        super().__init__()
        self.criterios = []
        criterio = Criterio("Desarrollo y profundidad en el tratamiento del tema", "", 0.20 )
        self.criterios.append( criterio )
        criterio = Criterio("Desafio academico y cientifico del tema", "", 0.15)
        self.criterios.append(criterio)
        criterio = Criterio("Cumplimiento de los objetivos propuestos", "", 0.10)
        self.criterios.append(criterio)
        criterio = Criterio("Creatividad e innovacion de las soluciones y desarrollos propuestos", "" , 0.10)
        self.criterios.append(criterio)
        criterio = Criterio("Validez de los resultados y concluciones", "", 0.20)
        self.criterios.append(criterio)
        criterio = Criterio("Manejo y procedimiento de la informacion y bibliografia", "", 0.10)
        self.criterios.append(criterio)
        criterio = Criterio("Calidad y presentacion del documento escrito ", "", 0.075)
        self.criterios.append(criterio)
        criterio = Criterio("Presentacion oral", "", 0.075)
        self.criterios.append(criterio)

    def agregar_criterios(self, criterios_obj):
        self.criterios.append(( criterios_obj ))