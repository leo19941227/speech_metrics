from pathlib import Path
from setuptools import setup, find_packages

here = Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name='speech_metrics',
    version='0.2.2',
    url='https://github.com/leo19941227/speech_metrics',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Shu-wen Yang',
    author_email='leo19941227@gmail.com',
    description='A lightweight package for common metrics in speech processing',
    license='MIT License',
    packages=find_packages(),
    install_requires=[
        "editdistance",
        "pb_bss_eval",
        "sacrebleu",
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
