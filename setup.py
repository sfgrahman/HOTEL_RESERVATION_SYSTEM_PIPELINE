from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name ="HOTEL-RESERVATION-SYSTEM",
    version="0.1",
    author="Moududur Shamim",
    author_email="sfgrahman35@gmail.com",
    packages=find_packages(),
    install_requires =requirements,
)