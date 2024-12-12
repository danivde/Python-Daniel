import pytz
# Establece tu zona horaria, por ejemplo, 'America/New_York'
zona_horaria = pytz.timezone('Europe/Madrid')
# Obtiene la hora actual en tu zona horaria
hora_actual = datetime.now(zona_horaria)
print(hora_actual)
