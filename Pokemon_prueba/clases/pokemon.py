#LIBRERIAS
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gestores.puente_json import datos_pokemones




class Pokemon:
    #ATRIBUTOS
    def __init__(self,id_especie,nivel):
        #EXTRAER DATOS DE PUENTE_JSON
        datos_especie = datos_pokemones[id_especie]
        datos_especie_base = datos_especie["base"]

        #VARIABLES SELF
        self.id_especie = id_especie
        self.nivel = nivel
        #ESTADISTICAS BASE
        self.nombre = datos_especie["nombre"]
        self.tipos = datos_especie["tipos"]
        self.vida = datos_especie_base["ps"]
        self.ataque = datos_especie_base["ataque"]
        self.defensa = datos_especie_base["defensa"]
        self.velocidad = datos_especie_base["velocidad"]
        self.ataque_especial = datos_especie_base["ataque_especial"]
        self.defensa_especial = datos_especie_base["defensa_especial"]
        


    #CALCULOS
    def calcular_ps(self):
        pass

    def calcular_ataque(self):
        pass


    #METODOS DE COMBATE BASICO
    def recibir_daño(self):
        pass

    def inflifir_daño(self):
        pass

    #COMPROBACIONES E INFO
    def esta_vivo(self):
        pass

    def mostrar_stats(self):
        texto_intro = "\n" + "="*20 + f"DATOS DE {self.nombre}" + "="*20
        print(texto_intro)
        print(f"ID: {self.id_especie}. Nombre: {self.nombre}")
        print(f"Tipos: {self.tipos}")
        print("")
        print("Estadísticas:")
        print(f"Nivel: {self.nivel}")
        print(f"Vida: {self.vida}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Velocidad: {self.velocidad}")
        print(f"Ataque esp: {self.ataque_especial}")
        print(f"Defensa esp: {self.defensa_especial}")
        print("="*len(texto_intro))


pk1 = Pokemon("001","1")
pk1.mostrar_stats()