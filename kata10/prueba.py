#def water_left(astronauts, water_left, days_left):
#    daily_usage = astronauts * 11
#    total_usage = daily_usage * days_left
#    total_water_left = water_left - total_usage
#    #return f"Agua total restante en {days_left} días es: {total_water_left} litros"
#    if total_water_left < 0:
#        raise RuntimeError(f"No hay suficiente agua para  {astronauts} astronautas después de {days_left} días!")
#    return f"Agua total restante en {days_left} días es: {total_water_left} litros"
#print(water_left(5, 100, 2))

def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            argument / 10
        except TypeError:
            #Si no se recibe un argumento que sea int, arrojará:
            raise TypeError(f"Todos los argumentos deben ser formato int, pero se recibió: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"No hay suficiente agua para  {astronauts} astronautas después de {days_left} días!")
    return f"Agua total restante en {days_left} días es: {total_water_left} litros"
print(water_left(5, 100, None))