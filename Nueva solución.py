def preparar_solucion():
    # Solicitar al usuario las concentraciones de las dos soluciones
    c1 = float(input("Ingrese la concentración de la primera solución (%): "))
    c2 = float(input("Ingrese la concentración de la segunda solución (%): "))
    
    # Solicitar al usuario la concentración y el volumen final deseado
    cf = float(input("Ingrese la concentración final deseada (%): "))
    vf = float(input("Ingrese el volumen final deseado (mL): "))
    
    # Sistema de ecuaciones
    # c1*x + c2*y = cf*vf
    # x + y = vf
    # Resolviendo para x y y
    # x = (cf - c2) * vf / (c1 - c2)
    # y = vf - x
    
    try:
        x = (cf - c2) * vf / (c1 - c2)
        y = vf - x
        
        if x < 0 or y < 0:
            raise ValueError("No es posible preparar la solución con las concentraciones proporcionadas.")
        
        print(f"Debe mezclar {x:.2f} mL de la solución de {c1}% y {y:.2f} mL de la solución de {c2}%.")
    except ZeroDivisionError:
        print("Las concentraciones de las soluciones no deben ser iguales.")
    except ValueError as e:
        print(e)

# Ejecutar la función
preparar_solucion()