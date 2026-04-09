from pathlib import Path
from PIL import Image
from config import t

def compress_image(input_path: Path, output_dir: Path, config):
    """
    Procesa una imagen individual aplicando los parámetros de configuración (ImgZ).
    Esta es la función principal donde se aplicará la lógica compleja de compresión/redimensión.
    """
    file_type = input_path.suffix.lower()
    lang = config['lang']

    print(t('processing', lang=lang, filename=input_path.name))

    try:
        img = Image.open(input_path)

        # 1. Aplicar Redimensionamiento (Si está configurado)
        if config['max_dimension'] is not None and (img.width > config['max_dimension'] or img.height > config['max_dimension']):
            print(t('dimension_info', lang=lang, max_dim=config['max_dimension']))
            img.thumbnail((config['max_dimension'], config['max_dimension']))

        # 2. Determinar formato y parámetros de guardado
        save_params = {}
        output_path = output_dir / input_path.name # Mantener el nombre original en la salida

        if file_type in ['.jpg', '.jpeg']:
            # Compresión JPEG con calidad configurable
            quality = config['jpg_quality']
            print(t('jpeg_quality', lang=lang, quality=quality))
            save_params['quality'] = quality

        elif file_type == '.png':
            # Para PNG, la compresión es diferente; aquí solo se mantiene la funcionalidad.
            print(t('png_info', lang=lang))
        else:
            print(t('unsupported', lang=lang, file_type=file_type))
            return False

        # 3. Guardar el resultado comprimido
        img.save(output_path, **save_params)
        print(t('success', lang=lang, output=output_dir.name, filename=input_path.name))
        return True

    except Exception as e:
        print(t('failed', lang=lang, filename=input_path.name, error=e))
        return False

def process_batch(input_path: Path, output_path: Path, config):
    """
    Procesa por lotes todas las imágenes en un directorio.

    Returns:
        int: Número de imágenes procesadas exitosamente
    """
    lang = config['lang']

    print("\n" + t('separator', lang=lang))
    print(t('processing_start', lang=lang))
    print(t('config_info', lang=lang, quality=config['jpg_quality'], max_dim=config['max_dimension'] if config['max_dimension'] else 'None'))
    print(t('separator', lang=lang))

    processed_count = 0
    for file_path in input_path.iterdir():
        if file_path.suffix.lower() in ['.jpg', '.jpeg', '.png']:
            success = compress_image(file_path, output_path, config)
            if success:
                processed_count += 1

    print("\n" + t('separator', lang=lang))
    print(t('processing_complete', lang=lang))
    print(t('success_count', lang=lang, count=processed_count))
    print(t('results_saved', lang=lang, path=output_path))
    print(t('separator', lang=lang))

    return processed_count
