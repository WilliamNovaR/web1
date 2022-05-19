from fpdf import FPDF


class PDF(FPDF):
    #variables para guardar los datos individuales de cada acta y generar el pdf
    fuente = ''
    inicializar = ''
    nombre_pdf = ''
    fecha = ''
    num_acta = ''
    titulo = 'Trabajo de grado denominado: "'
    autor = ''
    id = ''
    periodo = ''
    director = ''
    codirector = ''
    enfasis = ''
    modalidad = ''
    jurado1 = ''
    jurado2 = ''
    num_criterio = ''
    nombre_criterio = ''
    ponderacion = ''
    calificacion = ''
    observacion = ''
    calificacion_final = ''
    unidad = ''
    decima = ''
    comentario_final = ''
    correcciones = ''
    recomendacion = ''
    #funcion que crea el encabezado del pdf
    def header(self):
        self.image( "img.png", 10, 8, 33 )
        self.set_font(family= self.fuente, size= 20, style= 'B' )
        self.cell(0, 3, 'Facultad de ingenieria', border=False, ln=1, align= 'C' )
        self.cell(0, 15, 'Maestria en ingenieria', border=False, ln=1, align='C')
        self.set_font( family = self.fuente, style = 'B', size= 13)
        self.cell(1, -5, 'ACTA: ' + self.num_acta, border=False, ln=0, align='L')
        self.cell(0, -5, 'Fecha: ' + self.fecha , border=False, ln=1, align='R')
        self.ln(20)
    #funcion que imprime en el acta los datos inicializados por el asistente
    def datos(self):
        self.set_font( family = self.fuente, style = 'B', size= 15)
        self.cell(0, 13, 'ACTA DE EVALUACIÓN DE TRABAJO DE GRADO', border=False, ln=1, align='C')
        self.set_font( family = self.fuente, style = '', size= 12)
        self.multi_cell(0, 6, txt = self.titulo , border=False, align='l')
        self.cell( 25, 10, 'Autor: ', border=False, ln = 0, align= "L" )
        self.cell(50, 10, txt = self.autor , border=False, ln=0, align="L")
        self.cell(10, 10, 'ID: ' + self.id, border=False, ln=1, align="L")
        self.cell(25, 10, 'Periodo: ', border=False, ln=0, align="L")
        self.cell(10, 10, txt = self.periodo, border=False, ln=1, align="L")
        self.cell(25, 10, 'Director: ', border=False, ln=0, align="L")
        self.cell(10, 10, txt=self.director, border=False, ln=1, align="L")
        self.cell(25, 10, 'Enfasis en: ', border=False, ln=0, align="L")
        self.cell(10, 10, txt=self.enfasis, border=False, ln=1, align="L")
        self.cell(25, 10, 'Coirector: ', border=False, ln=0, align="L")
        self.cell(10, 10, txt=self.codirector, border=False, ln=1, align="L")
        self.cell(25, 10, 'Enfasis en: ', border=False, ln=0, align="L")
        self.cell(10, 10, txt=self.enfasis, border=False, ln=1, align="L")
        self.cell(25, 10, 'Modalidad: ', border=False, ln=0, align="L")
        self.cell(10, 10, txt=self.modalidad, border=False, ln=1, align="L")
        self.cell(25, 10, 'Jurado1: ', border=False, ln=0, align="L")
        self.cell(10, 10, txt=self.jurado1, border=False, ln=1, align="L")
        self.cell(25, 10, 'Jurado2: ', border=False, ln=0, align="L")
        self.cell(10, 10, txt=self.jurado2, border=False, ln=1, align="L")
    #funcion creada para imprimir en el acta una texto importante
    def extra(self):
        self.multi_cell(0, 5, 'En atención al desarrollo de este Trabajo de Grado y al documento y sustentación que presentó el(la) autor(a), los Jurados damos las siguientes calificaciones parciales y observaciones (los criterios a evaluar y sus ponderaciones se estipulan en el artículo 7.1 de las Directrices para Trabajo de Grado de Maestría):', border=False, align='l')
    #funcion que imprime la evaluacion de los jurados de cada criterio
    def criterio(self):
        self.set_font( family = self.fuente, style = 'B', size= 12)
        self.cell(5, 10, txt = self.num_criterio, border=False, ln=0, align="L")
        self.cell(10, 10, txt=self.nombre_criterio, border=False, ln=1, align="L")
        self.set_font( family = self.fuente, style = '', size= 12)
        self.cell(38, 10, 'Calificacion parcial: ', border=False, ln=0, align="L")
        self.cell(145, 10, txt=self.calificacion, border=False, ln=0, align="L")
        self.cell(10, 10, txt=self.ponderacion, border=False, ln=1, align="R")
        self.multi_cell(0, 15, txt=self.observacion, border=False, align='L')
        self.multi_cell(0, 10, '____________________________________________________________________________________________________________________________________________________________________', border=False, align='l')
    #funcion que imprime las calificaciones finales del jrado
    def nota_final(self):
        self.set_font( family = self.fuente, style = 'B', size= 12)
        self.multi_cell(0, 10, 'Como resutado de estas calificaciones parciales y sus ponderaciones, la calificacion del trabajo de grado es: ' + self.calificacion_final, border=False, align="L")
        self.cell(54, 10, '', border=False, ln=0, align="L")
        self.cell(70, 5, txt= self.calificacion_final, border=False, ln=0, align="L")
        #esta parte sirve para dar el numero de la nota en letras
        entero = float(self.calificacion_final) // 1.0
        decima = round(float(self.calificacion_final) - entero, 1)
        if entero == 0:
            self.unidad = 'Cero'
        elif entero == 1:
            self.unidad = 'Uno'
        elif entero == 2:
            self.unidad = 'Dos'
        elif entero == 3:
            self.unidad = 'Tres'
        elif entero == 4:
            self.unidad = 'Cuatro'
        elif entero == 5:
            self.unidad = 'Cinco'
        if decima == 0.0:
            self.decima = 'Cero'
        elif decima == 0.1:
            self.decima = 'Uno'
        elif decima == 0.2:
            self.decima = 'Dos'
        elif decima == 0.3:
            self.decima = 'Tres'
        elif decima == 0.4:
            self.decima = 'Cuatro'
        elif decima == 0.5:
            self.decima = 'Cinco'
        elif decima == 0.6:
            self.decima = 'Seis'
        elif decima == 0.7:
            self.decima = 'Siete'
        elif decima == 0.8:
            self.decima = 'Ocho'
        elif decima == 0.9:
            self.decima = 'Nueve'
        self.cell(0, 5, txt= self.unidad + ' punto ' + self.decima, border=False, ln=1, align="L")
        self.cell(49, 10, '', border=False, ln=0, align="L")
        self.cell(86, 5, 'Número' , border=False, ln=0, align="L")
        self.cell(70, 10, 'Letra', border=False, ln=1, align="L")
        self.set_font( family = self.fuente, style = '', size= 12)
        self.multi_cell( 0, 6, txt = self.comentario_final, border=False, align='L' )
        self.cell(1, 8, '', border=False, ln=0, align="L")
        self.multi_cell(0, 6, '___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________' , border=False, align='L')
        self.cell(1, 8, '', border=False, ln=0, align="L")
        self.multi_cell(0, 6, txt = self.correcciones , border=False, align='L')
        self.cell(1, 8, '', border=False, ln=0, align="L")
        self.multi_cell(0, 6,'___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________', border=False, align='L')

    #la funcion crea la plantilla de las firmas
    def firmas(self):
        self.cell(40, 40, '', border=False, ln=0, align="L")
        self.set_font(  family = self.fuente, style = '', size = 12)
        self.cell(65, 13, '________________________', border=False, ln=0, align="L")
        self.cell(1, 13, '________________________', border=False, ln=1, align="L")
        self.cell(55, 25, '', border=False, ln=0, align="L")
        self.cell(65, 13, 'Firma jurado 1', border=False, ln=0, align="L")
        self.cell(1, 13, 'Firma jurado 2', border=False, ln=0, align="L")

    #esta funcion imprime los datos que se muestran en caso que la nota final del trabajo sea mayor a 4.5
    def extra(self):
        self.set_font( family = self.fuente, style = '', size= 12)
        self.cell(1, 5, '', border=False, ln=1, align="L")
        self.multi_cell(0, 8, 'En atención a que el Trabajo de Grado se distingue porque la calificación del trabajo es superior a 4,50 y se destaca por dos condiciones (que indicamos) de las siguientes tres como se estipula en el artículo 7.6 de las Directrices para Trabajo de Grado de Maestría:', border=False, align='L')
        self.cell(1, 5, '', border=False, ln=1, align="L")
        self.cell(1, 10, '  ' + chr(157) + '   El estudiante superó los objetivos propuestos. _____' , border=False, ln=1, align="L")
        self.cell(1, 10, '  ' + chr(157) + '   El estudiante demostró una profundidad destacable en el conocimiento y tratamiento del tema. _____', border=False, ln=1, align="L")
        self.cell(1, 10, '  ' + chr(157) + '   El tema ofrecía una dificultad superior a lo ordinario. ____',border=False, ln=1, align="L")
        self.cell(1, 3, '', border=False, ln=1, align="L")
        self.multi_cell(0, 8, 'Los Jurados recomendamos que el Consejo de la Facultad otorgue Mención de Honor a este Trabajo de Grado, y motivamos esta recomendación con base en las siguientes apreciaciones:', border=False, align='L')
        self.cell(1, 3, '', border=False, ln=1, align="L")
        self.multi_cell(0, 8, txt= self.recomendacion, border =False, align='L')
        self.cell(1, 3, '', border=False, ln=1, align="L")
        self.multi_cell(0, 10, '__________________________________________________________________________________', border=False, align='L')
        self.firmas()
        self.cell(1, 15, '', border=False, ln=1, align="L")
        self.set_font( family = self.fuente, style = 'B', size = 12)
        self.cell(1, 10, 'Decisión del Consejo de la Facultad:', border=False, ln=1, align="L")
        self.set_font( family = self.fuente, style = '', size = 12)
        self.multi_cell(0, 8, 'En virtud de las condiciones que indicaron los Jurados y su motivación, el Consejo de la Facultad decidió losiguiente:', border=False, align='L')
        self.cell(1, 5, '', border=False, ln=1, align="L")
        self.cell(1, 10, '  ' + chr(157) + '          El tema ofrecía una dificultad superior a lo ordinario. ____', border=False, ln=1, align="L")
        self.cell(1, 10, '  ' + chr(157) + '          No Conceder Mención de Honor al Proyecto de Grado____', border=False, ln=1, align="L")
        self.cell(1, 10, 'Tal y como se consigna en el Acta No. ___________ del Consejo de la Facultad.', border=False, ln=1, align="L")


