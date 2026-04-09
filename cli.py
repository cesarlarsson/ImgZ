import argparse
import sys
from pathlib import Path
from config import t
from image_processor import process_batch

def parse_arguments():
    """Configura y parsea los argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(
        description="ImgZ - CLI para compresión por lotes de imágenes (JPG/PNG).",
        epilog="Ejemplo: imgz --jpg-quality 85 --max-dimension 1200 /ruta/fotos"
    )

    # Argumento obligatorio: Directorio de entrada
    parser.add_argument(
        'input_dir',
        type=str,
        help='Ruta al directorio que contiene las imágenes a comprimir.'
    )

    # Argumentos opcionales de Configuración (Flags)
    parser.add_argument(
        '--output-dir',
        type=str,
        default='./compressed_images',
        help='Directorio donde se guardarán las imágenes comprimidas.'
    )
    parser.add_argument(
        '--jpg-quality',
        type=int,
        default=85,
        choices=range(1, 101), # Solo permite valores de 1 a 100
        metavar='[1-100]',
        help='Calidad de compresión para archivos JPEG (1-100). Por defecto: 85.'
    )
    parser.add_argument(
        '--max-dimension',
        type=int,
        default=None,
        help='Dimensiones máximas (ancho o alto) en píxeles para redimensionar la imagen.'
    )
    parser.add_argument(
        '--lang',
        type=str,
        default='es',
        choices=['es', 'en'],
        help='Idioma de los mensajes de salida (es/en). Por defecto: es.'
    )

    return parser.parse_args()

def validate_and_setup_paths(args):
    """
    Valida las rutas de entrada y salida, crea directorios necesarios.

    Returns:
        tuple: (input_path, output_path) como objetos Path
    """
    input_path = Path(args.input_dir).resolve()
    output_path = Path(args.output_dir).resolve()
    lang = args.lang

    if not input_path.is_dir():
        print(t('error_invalid_dir', lang=lang, path=input_path), file=sys.stderr)
        sys.exit(1)

    # Crear el directorio de salida si no existe
    output_path.mkdir(parents=True, exist_ok=True)
    print(t('output_configured', lang=lang, path=output_path))

    return input_path, output_path

def run():
    """Función principal que coordina la ejecución del CLI."""
    args = parse_arguments()
    input_path, output_path = validate_and_setup_paths(args)

    # Configuración para pasar a la función de procesamiento
    config = {
        'jpg_quality': args.jpg_quality,
        'max_dimension': args.max_dimension,
        'lang': args.lang
    }

    # Procesar las imágenes
    process_batch(input_path, output_path, config)
