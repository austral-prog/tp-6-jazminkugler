def add_ elements(lista):
	lista.insert(0, 'pink')
	lista.append('yellow')
	return lista

lista = ['Red', 'Green', 'White', 'Black']	
print(add_elements(lista))
def add_ elements(lista):
	lista.insert(0, 'pink')
	lista.append('yellow')
	return lista

lista = ['Red', 'Green', 'White', 'Black']	
print(add_elements(lista))

def remove_elements(lista_to_remove_elements):
    len_lista = len(lista_to_remove_elements)
    if len_lista >= 6:
        del lista_to_remove_elements [5]
        del lista_to_remove_elements [4]
        del lista_to_remove_elements [0]
        return lista_to_remove_elements
    elif len_lista  == 5:
        del lista_to_remove_elements [4]
        del lista_to_remove_elements [0]
        return lista_to_remove_elements
    elif len_lista == 2 or len_lista == 3 or len_lista == 4:      
        del lista_to_remove_elements [0]
        return lista_to_remove_elements
    else:
        return []
