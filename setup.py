from setuptools import setup, find_packages

setup(
    name='speech_metrics',
    version='0.1.0',
    url='https://github.com/leo19941227/speech_metrics',
    author='Shu-wen Yang',
    author_email='leo19941227@gmail.com',
    description='A lightweight package for common metrics in speech processing',
    packages=find_packages(),
    install_requires=[
        "editdistance",
        "pb_bss_eval",
    ],
)
