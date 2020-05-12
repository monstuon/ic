import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sugeno-pkg-monstuon", # Replace with your own username
    version="0.0.1",
    author="Daniel Albornoz",
    author_email="eldani.mdq@gmail.com",
    description="Takagi-Sugeno FIS",
    long_description="Implementación en Python de Sistema de inferencia difusa tipo Sugeno con clustering substractivo",
    long_description_content_type="text/markdown",
    url="https://github.com/monstuon/ic",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)