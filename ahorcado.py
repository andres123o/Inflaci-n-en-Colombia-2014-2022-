from cProfile import run
import json

info = """
    -------------------------------------------------------------------

    Hola, vamos a mostrarte la inflación de Colombia por año y mes 
    desde 2015 hasta la fecha, ingresa una fecha con el siguente formato
    Fecha: AÑO-MES (2021-02)

    -------------------------------------------------------------------
    """

print(info)



def runCode(data):
    with open('./datos/inflacion.json', 'r', encoding='utf-8') as f:
        dataTotal = json.load(f)
        l = 'Para esta fecha la inflacion total es de: '
        o = ' EA'
        u = """
---------------------------------------------
            Prueba con otra fecha
---------------------------------------------
        """
        print(l + dataTotal[data] + o + u)
        



for i in range(1, 100):
    timeData = input('Fecha: ')
    runCode(timeData)