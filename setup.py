from setuptools import setup, find_packages

setup(
    name="gita",
    version="0.1",
    packages=find_packages(),
    install_requires=["click", "g4f", "gitpython"],
    entry_points={
        "console_scripts": [
            "gita=gita.cli:cli",
        ],
    },
)

