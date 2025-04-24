from coche import Coche

class Coches():
    lista_coches = []

    def agregar_coche(self, coche):
        self.lista_coches.append(coche)
        print('Coche agregado correctamente.')

    def buscar_coche(self, matricula):
        for coche in self.lista_coches:
            if coche.matricula == matricula:
                return coche
        return None

    def eliminar_coche(self, matricula):
        coche = self.buscar_coche(matricula)
        if coche:
            self.lista_coches.remove(coche)
            print('Coche eliminado correctamente.')
        else:
            print('Coche no encontrado.')

    def existe_coche(self, matricula):
        for coche in self.lista_coches:
            if coche.matricula == matricula:
                return True
        return False

    def mostrar_coches(self):
        if not self.lista_coches:
            print('No hay coches registrados.')
        else:
            for coche in self.lista_coches:
                print(f'Matricula: {coche.matricula}, Marca: {coche.marca}, Modelo: {coche.modelo}, Color: {coche.color}')

