
#permite ver un resumen de las actas
def listar_actas(st, criterios_controller, acta_controller):
    st.title("Informacion resumen de acta")
    # se usan los arreglos para guardar los nombres y mostrarlos luego en un selecte box
    actas_nombres = []
    criterios = []
    for acta in acta_controller.actas:
        actas_nombres.append(acta.nombre_pdf)
    for criterio in criterios_controller.criterios:
        criterios.append(criterio.identificador)
    seleccionar_acta = st.selectbox("seleccioanr estudiante", actas_nombres)
    #imprime los datos de las actas resumidos
    for pdf in acta_controller.actas:
        if seleccionar_acta == pdf.nombre_pdf:
            st.subheader("Numero de acta: " + pdf.num_acta)
            st.subheader("Fecha: " + pdf.fecha)
            st.subheader("Nombre autor: " + pdf.autor)
            st.subheader("Nota: " + pdf.calificacion_final)
            if float(pdf.calificacion_final) > 3.5:
                st.success("Aprobado")
            else:
                st.error("Reprobado")

            st.subheader("Nombre director: " + pdf.director)
            st.subheader("Jurado1 : " + pdf.jurado1)
            st.subheader("Jurado2 : " + pdf.jurado2)
