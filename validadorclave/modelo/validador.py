from abc import ABC, abstractmethod


class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave: str) -> bool:
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave: str) -> bool:
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave: str) -> bool:
        return any(c.isdigit() for c in clave)

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)

    def contiene_caracter_especial(self, clave: str) -> bool:
        return any(c in '@_#$%' for c in clave)

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            return False
        if not self._contiene_mayuscula(clave):
            return False
        if not self._contiene_minuscula(clave):
            return False
        if not self._contiene_numero(clave):
            return False
        if not self.contiene_caracter_especial(clave):
            return False
        return True

class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(6)

    def contiene_calisto(self, clave: str) -> bool:
        clave_lower = clave.lower()
        if "calisto" not in clave_lower:
            return False

        indice = clave_lower.index("calisto")
        palabra_calisto = clave[indice:indice + 7]

        mayusculas = sum(1 for c in palabra_calisto if c.isupper())
        return 2 <= mayusculas < 7

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            return False
        if not self._contiene_numero(clave):
            return False
        if not self.contiene_calisto(clave):
            return False
        return True


class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)



