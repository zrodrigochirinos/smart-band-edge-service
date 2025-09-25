# Servicio de borde de banda inteligente (smart_band_edge_service)
 
## Descripción general
 
Smart Band Edge Service es una aplicación basada en Python para procesar y analizar datos de dispositivos portátiles inteligentes en el borde.
 
## Dependencias
- Python 3.13 o superior.
- Flask (marco web)
- Peewee (ORM para interacciones con bases de datos)
- SQLite (base de datos)
- python-dateutil (utilidades de fecha y hora)
 
## Estructura de diseño impulsado por el dominio (DDD)
El proyecto sigue un enfoque de diseño impulsado por el dominio (DDD), organizando el código en contextos delimitados distintos:
- **Monitoreo de la salud**: administra datos relacionados con la salud de las pulseras inteligentes, incluida la frecuencia cardíaca.
- **Gestión de identidad y acceso**: gestiona la autenticación y autorización del dispositivo.
 
## Historias de usuario
Las historias de usuario del servicio Smart Band Edge se pueden encontrar en el archivo [docs/user-stories.md](docs/user-stories.md).
 
## Diagrama de clases
El diagrama de clases del servicio Smart Band Edge está disponible en el archivo [docs/class-diagram.puml](docs/class-diagram.puml).