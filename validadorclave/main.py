from validadorclave.modelo.validador import ReglaValidacionGanimedes, ReglaValidacionCalisto, Validador


def validar_clave(clave, reglas):
    for regla in reglas:
        validador = Validador(regla)
        try:
            if validador.es_valida(clave):
                print(f"La clave es válida para la validación {regla.__class__.__name__}")
        except Exception as e:
            print(f"Error: {regla.__class__.__name__}: {str(e)}")


# Ejemplo de uso
if __name__ == "__main__":
    clave = input("Ingrese una clave para validar: ")
    reglas = [ReglaValidacionGanimedes(), ReglaValidacionCalisto()]
    validar_clave(clave, reglas)