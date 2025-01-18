def sumar(a, b):
    """
    Retorna la suma de a y b.
    """
    return a + b

def multiplicar(a, b):
    """
    Retorna el producto de a por b.
    """
    return a * b

def dividir(a, b):
    """
    Retorna la división de a entre b.
    Si b es cero, retorna un mensaje de error.
    """
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b
