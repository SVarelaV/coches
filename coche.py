class Coche:
    def __init__(self, matricula, marca, modelo, color):
        self._matricula = matricula
        self._marca = marca
        self._modelo = modelo
        self._color = color

    @property
    def matricula(self):
        return self._matricula
    @matricula.setter
    def matricula(self, nueva_matricula):
        self._matricula = nueva_matricula

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, nueva_marca):
        self._marca = nueva_marca

    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, nuevo_color):
        self._color = nuevo_color
