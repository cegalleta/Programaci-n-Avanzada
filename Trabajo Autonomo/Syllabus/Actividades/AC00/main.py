from collections import namedtuple, defaultdict


# Para esta parte necesitarás los contenidos de la semana 0
def cargar_datos(path):
    # Para esta función te puede servir el cuaderno 3 de la semana 0
    with open('ayudantes.csv','r') as data:
        ayudantes = []
        for row in data:
            ayudante = row.strip()
            ayudantes.append(ayudante)
    return ayudantes

# De aquí en adelante necesitarás los contenidos de la semana 1
def crear_ayudantes(datos):
    # Completar función
    ayudante = namedtuple('Ayudante', ['Nombre', 'Cargo', 'Usuario'])
    ayudantes = []
    for row in datos:
        ayudante_list = row.split(',')
        ayudantes.append(ayudante(ayudante_list[0],
                                  ayudante_list[1],
                                  ayudante_list[2])) 
    return ayudantes[1::]

def encontrar_cargos(ayudantes):
    # Completar función
    return None

def ayudantes_por_cargo(ayudantes):
    # Completar función
    cargos = ['Full Docencia', 'Full Tareas', 'HÃ\xadbrido Docencia', 'HÃ\xadbrido Tareas']
    full_docencia = []
    full_tareas = []
    hibrido_docencia = []
    hibrido_tareas = []
    for row in ayudantes:
        ayudante= row.split(',')
        if ayudante[1] == 'Full Docencia':
            full_docencia.append(ayudante[0])
        elif ayudante[1] == 'Full_Tareas':
            full_tareas.append(ayudante[0])
        elif ayudante[1] == 'HÃ\xadbrido Docencia':
            hibrido_docencia.append(ayudante[0])
        else:
            hibrido_tareas.append(ayudante[0])
    ayudantes_por_cargo = [full_docencia, full_tareas, hibrido_docencia, hibrido_tareas]
    ayudante_dic = dict(zip(cargos, ayudantes_por_cargo))
    return ayudante_dic


if __name__ == '__main__':
    datos = cargar_datos('ayudantes.csv')
    if datos is not None:
        print('Se lograron leer los datos')
    else:
        print('Debes completar la carga de datos')

    ayudantes = crear_ayudantes(datos)
    if ayudantes is not None:
        print('\nLos ayudantes son:')
        for ayudante in ayudantes:
            print(ayudante)
    else:
        print('\nDebes completar la creación de Ayudantes')

    cargos = encontrar_cargos(ayudantes)
    if cargos is not None:
        print('\nLos cargos son:')
        for cargo in cargos:
            print(cargo)
    else:
        print('\nDebes completar la búsqueda de Cargos')

    clasificados = ayudantes_por_cargo(ayudantes)
    if clasificados is not None:
        print('\nLos ayudantes por cargos son:')
        for cargo in clasificados:
            print(f'\n{cargo}')
            for ayudante in clasificados[cargo]:
                print(ayudante)
    else:
        print('\nDebes completar la clasificación de Ayudantes')
        