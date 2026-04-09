<div align="center">
  <img src="https://raw.githubusercontent.com/cesarlarsson/ImgZ/main/ImgZ.jpg" alt="ImgZ Logo" width="400"/>

  # ImgZ

  ### Compresión de imágenes rápida y sencilla desde la línea de comandos

</div>

## 🎯 Objetivo del Proyecto
**ImgZ** es una utilidad de línea de comandos (CLI) robusta y multiplataforma que permite comprimir por lotes (*bulk*) imágenes JPG y PNG. Diseñada para proporcionar la máxima simplicidad de uso en cualquier sistema operativo (Windows, macOS, Linux).

## ✨ Características Principales
*   **Procesamiento por Lotes:** Compresión masiva de archivos `.jpg` y `.png` dentro de una carpeta seleccionada.
*   **Separación de Datos:** Genera un directorio de salida dedicado para los resultados comprimidos, manteniendo el origen intacto.
*   **Control Avanzado (Configurable):** Permite ajustar parámetros críticos desde la CLI:
    *   `--output-dir [RUTA]`: Define el directorio de salida (por defecto: `./compressed_images`).
    *   `--jpg-quality [1-100]`: Define la calidad de compresión JPEG deseada (por defecto: 85).
    *   `--max-dimension [PIXELS]`: Redimensiona las imágenes para limitar su tamaño máximo (ancho o alto en píxeles).

## 💻 Stack Tecnológico
*   **Lenguaje:** Python 3.6+
*   **Librerías Clave:** `Pillow` (PIL Fork) para manipulación de imágenes; `argparse` para manejo robusto de argumentos CLI.
*   **Distribución:** Empaquetado como un paquete instalable con `setup.py` para crear el comando global **`imgz`**.

## 📋 Requisitos Previos
*   Python 3.6 o superior
*   pip (gestor de paquetes de Python)

## 📦 Instalación

### Opción 1: Instalación en Modo Desarrollo
```bash
# 1. Clonar o navegar al directorio del proyecto
cd /ruta/al/proyecto

# 2. Instalar las dependencias
pip install -r requirements.txt

# 3. Instalar el paquete en modo desarrollo
pip install -e .
```

### Opción 2: Instalación Estándar
```bash
# Desde el directorio del proyecto
pip install .
```

## 🚀 Uso

### Sintaxis Básica
```bash
imgz [OPCIONES] <directorio_entrada>
```

### Parámetros Disponibles

| Parámetro | Tipo | Por Defecto | Descripción |
|-----------|------|-------------|-------------|
| `input_dir` | Obligatorio | - | Ruta al directorio con las imágenes a comprimir |
| `--output-dir` | Opcional | `./compressed_images` | Directorio donde se guardarán las imágenes procesadas |
| `--jpg-quality` | Opcional | `85` | Calidad de compresión JPEG (1-100) |
| `--max-dimension` | Opcional | `None` | Dimensión máxima en píxeles (ancho o alto) |
| `--lang` | Opcional | `es` | Idioma de los mensajes (es/en) |

### Ejemplos de Uso

**Ejemplo 1: Compresión básica (valores por defecto)**
```bash
imgz ./mis_fotos
```
- Comprime todas las imágenes JPG/PNG de `./mis_fotos`
- Las guarda en `./compressed_images`
- Usa calidad JPEG de 85
- No redimensiona

**Ejemplo 2: Compresión con calidad personalizada**
```bash
imgz --jpg-quality 90 ./mis_fotos
```
- Comprime con calidad JPEG de 90 (mayor calidad)

**Ejemplo 3: Compresión con redimensionamiento**
```bash
imgz --max-dimension 1200 ./mis_fotos
```
- Redimensiona imágenes para que no excedan 1200px en ninguna dimensión
- Mantiene la proporción de aspecto

**Ejemplo 4: Configuración completa personalizada**
```bash
imgz --output-dir ./web_ready --jpg-quality 80 --max-dimension 1920 ./fotos_originales
```
- Lee imágenes de `./fotos_originales`
- Las guarda en `./web_ready`
- Comprime JPG con calidad 80
- Redimensiona a máximo 1920px

**Ejemplo 5: Usar mensajes en inglés**
```bash
imgz --lang en ./my_photos
```
- Todos los mensajes de salida se mostrarán en inglés

## 🏗️ Arquitectura del Proyecto

```
.
├── config.py             # Traducciones y configuración multilenguaje
├── image_processor.py    # Lógica de compresión y procesamiento por lotes
├── cli.py                # Parsing de argumentos y validación de rutas
├── image_compressor.py   # Punto de entrada principal (ejecutable)
├── setup.py              # Configuración de instalación
├── requirements.txt      # Dependencias del proyecto
├── .gitignore            # Archivos y carpetas excluidas de Git
├── README.md             # Documentación en español
└── README_EN.md          # Documentación en inglés
```

## 🔧 Desarrollo

### Estructura Modular del Código

**ImgZ** está diseñado con una arquitectura modular clara:

1. **`config.py`** (47 líneas)
   - Diccionario de traducciones multilenguaje
   - Función helper `t()` para internacionalización

2. **`image_processor.py`** (73 líneas)
   - `compress_image()`: Procesa una imagen individual
   - `process_batch()`: Coordina el procesamiento por lotes
   - Lógica de compresión y redimensionamiento

3. **`cli.py`** (77 líneas)
   - `parse_arguments()`: Parsing de argumentos CLI
   - `validate_and_setup_paths()`: Validación y setup de directorios
   - `run()`: Función principal de ejecución

4. **`image_compressor.py`** (10 líneas)
   - Punto de entrada principal del programa

### Ejecución en Modo Desarrollo
```bash
# Ejecutar directamente sin instalación
python image_compressor.py --jpg-quality 85 ./mis_fotos
```

## 📄 Licencia
Este proyecto es de código abierto y está disponible para uso libre.

---


