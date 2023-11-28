    # Funcion para validar en los botones de las calles y las carreras
def validation_numbers(is_carrera, is_add_button, number):
    result = True
    if is_carrera:
        upper_boundary = 15
        lower_boundary = 10
    else:
        upper_boundary = 55
        lower_boundary = 50
    
    if is_add_button:
        if number + 1 > upper_boundary :
            result = False
    else:
        if number - 1 < lower_boundary:
            result = False

    return result

    #Recorre los numeros de las calles y las carreras, y las imprime para verificar que esten bien
def set_number_in_nodes(): 
    number_carrera = 15
    number_calle = 55

    while number_carrera >= 10:
        while number_calle >= 50:
            print(number_carrera, number_calle)
            number_calle -= 1
        number_carrera -= 1
        number_calle = 55

# set_number_in_nodes()

def convert_node_number_in_calle_carrera(node):
    calle = 55 - (node // 6)
    carrera = 15 - (node % 6)
    return (calle, carrera)

# for i in range(36):
#     print(convert_node_number_in_calle_carrera(i))

