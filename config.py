# Translation dictionary for multi-language support
TRANSLATIONS = {
    'es': {
        'processing': '   -> Procesando: {filename}...',
        'dimension_info': '   [INFO] Dimensiones exceden el límite de {max_dim}px. Redimensionando.',
        'jpeg_quality': '   [INFO] Usando compresión JPEG con calidad: {quality}',
        'png_info': '   [INFO] Procesando como PNG (sin cambios de calidad específicos).',
        'unsupported': '   [ERROR] Tipo de archivo {file_type} no soportado.',
        'success': '   [EXITO] Compresión completada y guardada en: {output}/{filename}',
        'failed': '   [FALLO] No se pudo procesar {filename}. Error: {error}',
        'output_configured': '✅ Directorio de salida configurado en: {path}',
        'processing_start': '🚀 INICIANDO PROCESAMIENTO POR LOTES DE IMÁGENES',
        'config_info': '   Configuración: JPG Quality={quality}, Max Dim={max_dim}',
        'processing_complete': '✨ PROCESAMIENTO FINALIZADO ✨',
        'success_count': '✅ Éxito: Se procesaron {count} imágenes.',
        'results_saved': '📂 Resultados guardados en: {path}',
        'error_invalid_dir': 'ERROR: El directorio de entrada no existe o no es un directorio válido: {path}',
        'separator': '=====================================================',
    },
    'en': {
        'processing': '   -> Processing: {filename}...',
        'dimension_info': '   [INFO] Dimensions exceed limit of {max_dim}px. Resizing.',
        'jpeg_quality': '   [INFO] Using JPEG compression with quality: {quality}',
        'png_info': '   [INFO] Processing as PNG (no specific quality changes).',
        'unsupported': '   [ERROR] File type {file_type} not supported.',
        'success': '   [SUCCESS] Compression completed and saved to: {output}/{filename}',
        'failed': '   [FAILED] Could not process {filename}. Error: {error}',
        'output_configured': '✅ Output directory configured at: {path}',
        'processing_start': '🚀 STARTING BATCH IMAGE PROCESSING',
        'config_info': '   Configuration: JPG Quality={quality}, Max Dim={max_dim}',
        'processing_complete': '✨ PROCESSING COMPLETE ✨',
        'success_count': '✅ Success: {count} images processed.',
        'results_saved': '📂 Results saved to: {path}',
        'error_invalid_dir': 'ERROR: Input directory does not exist or is not a valid directory: {path}',
        'separator': '=====================================================',
    }
}

def t(key, lang='es', **kwargs):
    """Helper function for translations"""
    return TRANSLATIONS[lang][key].format(**kwargs)
