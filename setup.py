from setuptools import setup, find_packages

setup(
    name='imgz',
    version='0.1.1',
    description='ImgZ - Herramienta CLI para compresión de imágenes',
    py_modules=['image_compressor', 'image_processor', 'cli', 'config'],
    install_requires=[
        'Pillow'
    ],
    entry_points={
        'console_scripts': [
            'imgz = cli:run'
        ]
    },
    python_requires='>=3.6',
)
