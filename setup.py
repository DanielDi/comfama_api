from setuptools import setup, find_packages

setup(
    name="afiliados-api",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "pytest",
    ],
)
