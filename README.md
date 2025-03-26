# Seleccionadora automática de plátanos

Este repositorio contiene scripts y configuraciones diseñados para implementar un sistema automático basado en Raspberry Pi para procesar imágenes de plátanos, discriminar su grado de madurez y separarlos automáticamente.

## Objetivo

Crear un sistema eficiente y confiable que permita clasificar automáticamente plátanos según su grado de madurez mediante análisis de imágenes en tiempo real.

## Contenido del Repositorio

- **scripts/**: Incluye diversos scripts exploratorios que prueban distintos métodos de procesamiento y análisis de imágenes.
- **raspberry_pi_setup/**: Documentación y archivos de configuración específicos para configurar una Raspberry Pi con cámara y software necesario para realizar la tarea de clasificación en tiempo real.

## Tecnologías Utilizadas

- Python
- OpenCV
- Raspberry Pi OS
- TensorFlow (opcional, si se utilizan métodos avanzados de clasificación mediante redes neuronales)

## Configuración y Uso

### Requisitos Previos

- Raspberry Pi (modelo recomendado: Raspberry Pi 4)
- Cámara compatible con Raspberry Pi
- Python 3.x instalado
- Librerías necesarias:

```bash
pip install opencv-python numpy
```

### Instalación

Clona el repositorio:

```bash
git clone https://github.com/edwardo1239/seleccionadora-platanos.git
cd seleccionadora-platanos
```

### Ejecución

Para ejecutar un script específico:

```bash
python scripts/nombre_del_script.py
```

Sigue las instrucciones específicas contenidas en cada directorio para detalles adicionales.

## Estructura Recomendada

Si deseas expandir o mantener este proyecto, considera la siguiente estructura:

```plaintext
seleccionadora-platanos/
├── scripts/
│   ├── deteccion_basica.py
│   ├── analisis_color.py
│   └── clasificacion_redes_neuronales.py
├── raspberry_pi_setup/
│   ├── instalacion_dependencias.md
│   └── configuracion_camara.md
├── README.md
└── requirements.txt
```

## Contribuciones

Las contribuciones son bienvenidas. Realiza un fork del repositorio, desarrolla tu mejora y envía un pull request.

## Autor

- Edwardo1239

## Licencia

Este proyecto es de código abierto bajo la licencia MIT.

