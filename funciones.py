

def tiempo_decomp(objeto):
    objeto = objeto.lower()
    descomposicion = {
        "papel": "2 a 5 meses",
        "vidrio": "4,000 años o más",
        "plástico": "500 a 1,000 años",
        "lata de aluminio": "80 a 200 años",
        "cáscara de plátano": "2 a 10 días",
        "bolsa de plástico": "150 a 300 años",
        "botella de vidrio": "Infinito (no se descompone, pero puede reciclarse)",
        "neumático": "50 a 80 años",
        "colilla de cigarro": "10 a 12 años",
        "pañal desechable": "450 años",
        "madera pintada": "13 años",
        "cáscara de naranja": "6 meses",
        "pañuelo de papel": "2 a 4 semanas",
        "movil":"1000 años"
    }
    if objeto in descomposicion:
        tiempo = descomposicion[objeto]
        resultado = f"El tiempo de {objeto} es : {tiempo}"
        return resultado
    else:
        return "este objeto no esta en la base de datos"
    
    