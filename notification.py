'''
Programa de Notificaciones en Windows.
Creado por Oscar Lancheros.

Este script genera notificaciones Windows, bajo el supuesto de que la jornada laboral va
de las 08:00 a las 17:00 horas, con una hora de almuerzo a las 12:00 del mediodía.

A las 10:00 y 15:00 horas, se genera una notificación recordando que es hora de hacer una
pausa activa para estirar los músculos e hidratar el cuerpo y la cual se repite dos veces con
un intervalo de tiempo de 1 minuto.

A las 12:00, se genera una notificación informando que es hora de ir a almorzar, la cual al igual
que las anteriores, también se repite dos veces a intervalos de tiempo de un minuto.

A las 17:00, se genera la última notificación del día generada por el programa, informando
al usuario que es hora de terminar con la jornada laboral y salir a descansar. Esta notificación a
diferencia de las anteriores, se repite 5 veces.

Cada una de estas notificaciones queda en la pantalla por un lapso de 10 segundos apróximadamente.

Una vez que se han hecho las notificaciones del correspondiente día, el programa entra en modo
de espera por un tiempo de 17 horas y vuelve a lanzar las respectivas notificaciones.

Para que este programa funcione, es necesario tener instaladas las librerías datetime para el
manejo de las horas y pyler para la generación de las notificaciones en Windows.

'''

#*------ Librerias necesarias ------*#

import time
from datetime import datetime, date, timedelta
from plyer import notification


#*------ Definición de notificaciones ------*#

'''
#! Acá se definen los tres tipos de notificaciones que se van a mostrar en pantalla.
'''

notificationMessage1 = 'Estira tus músculos e hidrata tu cuerpo'
notificationMessage2 = 'Es tiempo de ir a almorzar'
notificationMessage3 = 'Es tiempo de ir a descansar\nMañana será otro día'

#*------ Definición de Variables ------*#

'''
#! Para la librería <<datetime>> la fecha por default es: 1900-01-01T00:00:00.000,
#! por lo cual es necesario definir el año (yy), el mes (mm) y el día (dd).

#! Adicionalmente, se definen las variables para los intervalos de las pausas
#! activas, hora de almuerzo y fin de jornada laboral.
'''

currentDay = date.today()

yy = currentDay.year
mm = currentDay.month
dd = currentDay.day

activePause1 = datetime(yy, mm, dd, 10, 0, 0)
activePause1End = datetime(yy, mm, dd, 10, 3, 0)

lunchTimeStart = datetime(yy, mm, dd, 12, 0, 0)
lunchTimeEnd = datetime(yy, mm, dd, 12, 3, 0)

activePause2 = datetime(yy, mm, dd, 15, 0, 0)
activePause2End = datetime(yy, mm, dd, 15, 3, 0)

endTime = datetime(yy, mm, dd, 17, 0, 0)
endTimeEnd = datetime(yy, mm, dd, 17, 5, 0)


#*------ Función para calcular tiempo de espera ------*#

'''
#! Esta función se encarga de calcular el tiempo de espera entre una pausa y la siguiente.
'''

def waitingTime(time1, time2):
    difTime = time1 - time2
    delayTime = int(difTime.total_seconds())
    #print('tiempo de espera ' + str(delayTime) + ' s')
    time.sleep(delayTime)


#*------ PROGRAMA PRINCIPAL ------*#

if __name__ == "__main__":

    while True:

        #! Revisa la hora del sistema y comienza la ejecución del ciclo según las condiciones impuestas.

        actualTime = datetime.now()

        if actualTime < activePause1:
            waitingTime(activePause1, actualTime)

        elif actualTime >= activePause1 and actualTime < activePause1End:
            notification.notify(
                title="ES HORA DE LA PAUSA ACTIVA de las {}\n".format(
                    datetime.now().strftime("%H:%M:%S")),
                message=notificationMessage1,
                app_icon="brain2.ico",
                timeout=30
            )

            time.sleep(60)

        elif actualTime < lunchTimeStart:
            waitingTime(lunchTimeStart, actualTime)

        elif actualTime >= lunchTimeStart and actualTime < lunchTimeEnd:
            notification.notify(
                title="HORA DE ALMUERZO {}\n".format(
                    datetime.now().strftime("%H:%M:%S")),
                message=notificationMessage2,
                app_icon="brain2.ico",
                timeout=30
            )

            time.sleep(60)

        elif actualTime < activePause2:
            waitingTime(activePause2, actualTime)

        elif actualTime >= activePause2 and actualTime < activePause2End:
            notification.notify(
                title="ES HORA DE LA PAUSA ACTIVA de las {}\n".format(
                    datetime.now().strftime("%H:%M:%S")),
                message=notificationMessage1,
                app_icon="brain2.ico",
                timeout=30
            )

            time.sleep(60)

        elif actualTime < endTime:
            waitingTime(endTime, actualTime)

        elif actualTime >= endTime and actualTime <= endTimeEnd:
            notification.notify(
                title="ES HORA DE DESCANSAR {}\n".format(
                    datetime.now().strftime("%H:%M:%S")),
                message=notificationMessage3,
                app_icon="brain2.ico",
                timeout=30
            )

            time.sleep(60)

        #! Una vez terminado el ciclo de las pausas, las variables de tiempo son actualizadas
        #! sumándoles un día a cada una y luego calcula el tiempo de espera para comenzar el
        #! ciclo de notificaciones del siguiente día.

        elif actualTime > endTimeEnd:
            activePause1 = activePause1 + timedelta(days=1)
            activePause1End = activePause1End + timedelta(days=1)
            lunchTimeStart = lunchTimeStart + timedelta(days=1)
            lunchTimeEnd = lunchTimeEnd + timedelta(days=1)
            activePause2 = activePause2 + timedelta(days=1)
            activePause2End = activePause2End + timedelta(days=1)
            endTime = endTime + timedelta(days=1)
            endTimeEnd = endTimeEnd + timedelta(days=1)

            print(activePause1)
            print(lunchTimeStart)
            print(activePause2)
            print(endTime)

            waitingTime(activePause1, actualTime)

        else:
            break

