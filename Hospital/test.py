from Personas.enfermero import Enfermero
from Personas.recepcionista import Recepcionista
from Personas.paciente import Paciente
from Personas.doctor import Doctor
from Hospital.hospital import Hospital
from datetime import datetime
from UnidadesMedicas.unidadmedica import UnidadMedica
from console import Console


Hospital_Prado = Hospital("Hospital Del Prado", "Calle 123, Avenida ABC, Tijuana, B.C.", "6645678643", 1000)

unidad_pediatria = UnidadMedica(nombre="Pediatria", capacidad=150)
unidad_oncologia = UnidadMedica(nombre="Oncologia", capacidad=200)

Enfermero_1 = Enfermero("12345678", posicion= "Enfermero", fecha_de_empleo= datetime(2021,3,29), departamento="Pediatria",
              horario={"Lunes" : "7am - 3pm", "Martes" : "7am - 3pm", "Jueves" : "7am - 3pm"},
              telefono="6611250321", correo="enfermero1@hotmail.com", nombre="Michelle", apellido="Muñiz",
              fecha_nacimiento=datetime(1985, 6, 13), sexo="Mujer")

Enfermero_2 = Enfermero("ABC123", posicion= "Enfermero", fecha_de_empleo= datetime(2021,3,29), departamento="Oncologia",
              horario={"Lunes" : "7am - 3pm", "Miercoles" : "7am - 3pm", "Sabado" : "3pm - 9pm"},
              telefono="6616120055", correo="enfermero2@hotmail.com", nombre="Melany", apellido="Palomares",
              fecha_nacimiento=datetime(1980, 10, 4), sexo="Mujer")

Doctor_1 = Doctor(especialidad="Oncologo Infantil", cedula="13579", posicion="Doctor", fecha_de_empleo=datetime(2021, 3, 6), departamento="Oncologia",
           horario={"Martes" : "7am - 3pm", "Miercoles" : "7am - 3pm", "Sabado" : "7am - 3pm"},
           telefono="6615276357", correo="lmao@hotmail.com", nombre="Ximena", apellido="Gonzalez",
           fecha_nacimiento=datetime(1979, 1, 29), sexo="Mujer")

Doctor_2 = Doctor(especialidad="Pediatra", cedula="246810", posicion="Doctor", fecha_de_empleo=datetime(2021, 3, 6), departamento="Pediatria",
           horario={"Lunes" : "7am - 3pm", "Martes" : "7am - 3pm", "Viernes" : "7am - 3pm"},
           telefono="6615276357", correo="lmao@hotmail.com", nombre="Stephanie", apellido="Gonzalez",
           fecha_nacimiento=datetime(1980, 1, 29), sexo="Mujer")

Recepcionista_1 = Recepcionista(posicion="Recepcionista", fecha_de_empleo=datetime(2021,1,16), departamento="Oncologia",
                  horario={"Martes" : "7am - 3pm", "Miercoles" : "7am - 3pm", "Sabado" : "7am - 3pm"},
                  telefono="6618509876", correo="lol@hotmail.com", nombre="Andrea", apellido="Veleta",
                  fecha_nacimiento=datetime(1990, 8, 3), sexo="Mujer")

Recepcionista_2 = Recepcionista(posicion="Recepcionista", fecha_de_empleo=datetime(2021,1,16), departamento="Oncologia",
                  horario={"Martes" : "7am - 3pm", "Miercoles" : "7am - 3pm", "Sabado" : "7am - 3pm"},
                  telefono="6618509876", correo="lol@hotmail.com", nombre="Olivia", apellido="Esquivel",
                  fecha_nacimiento=datetime(1990, 3, 3), sexo="Mujer")

Paciente_1 = Paciente(razon_visita="Dolor Estomago", nombre="Mariana", apellido="Zamora", fecha_nacimiento=datetime(2002, 4, 6),
             sexo="Mujer")

Paciente_2 = Paciente(razon_visita="Hombro Esguinzado", nombre="Vanesa", apellido="Perez", fecha_nacimiento=datetime(2002, 12, 12),
             sexo="Mujer")

Doctor_1.agregar_evento_calendario("Cita Semanal", datetime(2021, 5, 6), "10am", f"{Paciente_1.nombre} {Paciente_1.apellido} {Paciente_1.id_paciente}")
Doctor_2.agregar_evento_calendario("Cita Mensual", datetime(2021, 4, 30), "7pm", f"{Paciente_2.nombre} {Paciente_2.apellido} {Paciente_2.id_paciente}")
Enfermero_1.agregar_evento_calendario("Vacunacion INFLUENZA", datetime(2021, 4, 28), "9am")
Enfermero_2.agregar_evento_calendario("Vacunacion COVID", datetime(2021, 4, 20), "7am")
Recepcionista_1.agregar_evento_calendario("Tour facilidades a nuevos empleados", datetime(2021, 5, 12), "11am")

Hospital_Prado._autenticador_admin.agregar_usuario("lol", "pass1234")
Hospital_Prado._autenticador_admin.agregar_usuario("lmao", "pass1234")

Hospital_Prado.agregar_doctor(Doctor_1)
Hospital_Prado.agregar_doctor(Doctor_2)

Hospital_Prado.agregar_enfermero(Enfermero_1)
Hospital_Prado.agregar_enfermero(Enfermero_2)

Hospital_Prado.agregar_recepcionista(Recepcionista_1)
Hospital_Prado.agregar_recepcionista(Recepcionista_2)

Hospital_Prado.agregar_unidad_medica(unidad_pediatria)
Hospital_Prado.agregar_unidad_medica(unidad_oncologia)

Recepcionista_1.registrar_paciente_en_hospital(Paciente_1, Hospital_Prado)
Recepcionista_2.registrar_paciente_en_hospital(Paciente_2, Hospital_Prado)

Doctor_1.agregar_paciente_a_lista_de_pacientes(Paciente_1)
Doctor_1.crear_receta_para_paciente(Hospital_Prado,Paciente_1, nombre_medicamento="Paracetamol", diagnostico_paciente="Dolor estomacal",
                             dosis="1 cada 12 horas", via_de_administracion="Pastilla", duracion_tratamiento="3 dias")

Doctor_2.agregar_paciente_a_lista_de_pacientes(Paciente_2)
Doctor_2.crear_diagnostico_de_paciente(Hospital_Prado,Paciente_2,diagnosis="Colitis Ulcerosa", sintomas=["Colicos", "Fiebre", "Fatiga"],
                                resultados_estudios=["Niveles altos de estres", "Factores geneticos"],
                                tratamiento="Tomar mucha agua. Tomar Corticoesteroides.")

Recepcionista_1.agendar_cita(Doctor_2,Paciente_2, "Cheque Resultados Estudios", datetime(2021,5,8), "12pm")

Console(Hospital_Prado)





