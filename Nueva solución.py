# Autor: Jorge Menéndez S.
# Licencia: MIT License
#
# Copyright (c) 2024 Jorge Menéndez S.
#
# Por la presente se concede permiso, sin cargo, a cualquier persona que obtenga una copia
# de este software y los archivos de documentación asociados (el "Software"), para tratar
# en el Software sin restricciones, incluyendo sin limitación los derechos
# para usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender
# copias del Software, y para permitir a las personas a quienes se les proporcione el Software
# hacerlo, sujeto a las siguientes condiciones:
#
# El aviso de copyright anterior y este aviso de permiso se incluirán en todas
# las copias o partes sustanciales del Software.
#
# EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA,
# INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD,
# IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O
# LOS TITULARES DEL COPYRIGHT SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑO U OTRA RESPONSABILIDAD,
# YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO MODO, QUE SURJA DE,
# FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS TRATOS EN EL
# SOFTWARE.

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
