from setuptools import setup, find_packages


with open("README.md", "r", errors="ignore") as f:
    long_description = f.read()

setup(
    name="vsi2tif",
    version="0.1.6",
    author="André Pedersen, Sebastian Krossa, Erik Smistad, David Bouget",
    author_email="andrped94@gmail.com",
    license="MIT",
    description="A package for converting images from cellSens VSI format to tiled, pyramidal TIFF",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andreped/vsi2tif",
    include_package_data=True,
    packages=find_packages(exclude=("figures")), 
    entry_points={
        "console_scripts": [
            "vsi2tif = vsi2tif.vsi2tif:main",
        ]
    },
    install_requires=["tqdm", "numpy"],
    extras_require={"dev": [
        "wheel",
        "setuptools",
        "black==22.3.0",
        "isort==5.10.1",
        "flake8==4.0.1",
    ]},
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
