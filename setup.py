
from setuptools import setup, find_packages

setup(
    name='poacher-catcher',
    version='0.1.0',
    description='',
    long_description='',
    author='',
    author_email='',
    url="",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'google-assistant-library>=1.0.1',
        'google-assistant-grpc>=0.2.0',
        'google-auth>=1.5.1',
        'google-auth-oauthlib>=0.2.0',
        'google-cloud-speech>=0.36.0',
        'gpiozero',
        'protobuf>=3.6.1',
        'picamera',
        'Pillow',
        'RPi.GPIO',
    ],
    python_requires='>=3.5.3',
)
