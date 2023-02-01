# Programa de Notificaciones en Windows
El objetivo de este programa es generar notificaciones de pausas activas, hora de almuerzo y terminación de la jornada laboral.

El programa esta diseñado bajo el supuesto de una jornada laboral de 8 horas, comenzando a las 8:00 horas y terminando a las 17:00 horas, con dos pausas activas, una a las 10:00 horas y la otra a las 15:00 horas y la hora de almuerzo a las 12:00 horas.

Una vez ejecutado, el programa revisará la hora del sistema y en base a las condiciones impuestas definirá el tiempo de espera necesario para lanzar la notificación que se encuentre más cerca a la hora del sistema. Las notificaciones de pausa activa y almuerzo se repiten dos veces en un lapso de tiempo de 2 minutos, mientras que la notificación de terminación de jornada laboral, se repite 5 veces en un lapso de 5 minutos. Una vez que se han ejecutado todas las notificaciones, el programa actualizará cada una de las variables de tiempo para notificación, sumándoles un día y luego calculará el tiempo que tiene que durar en espera el sistema para volver a comenzar el ciclo de notificaciones.

Para que este programa funcione, es necesario tener instaladas las librerías <s>datetime</s> para el manejo de las horas y <s>pyler</s> para la generación de las notificaciones en Windows, las cuales se pueden instalar con <s>pip.</s>

