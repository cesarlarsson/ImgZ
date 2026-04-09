from setuptools import setup, find_packages

setup(
    name='imgz',
    version='1.0.0',
    description='ImgZ - Herramienta CLI para compresión de imágenes',
    packages=find_packages(),
    install_requires=[
        'Pillow'
    ],
    entry_points={
        'console_scripts': [
            'imgz = image_compressor:main'
        ]
    },
    python_requires='>=3.6',
)
