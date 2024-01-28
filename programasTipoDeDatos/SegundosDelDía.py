

hora = int(input("Ingresa una hora('sin los minutos'): "))
minutos = int(input("Ingrese los minutos de la hora: "))

calculo = hora * 60 *60 + (minutos * 60)


print("Ingreso la hora",hora,"con",minutos,"minutos","\nHan pasado",calculo,"segundos desde que empezó el día")

