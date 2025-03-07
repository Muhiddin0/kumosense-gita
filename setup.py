from setuptools import setup, find_packages

setup(
    name="gita",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "gita=gita.cli:cli",
        ],
    },
    author="Sizning Ismingiz",
    author_email="your_email@example.com",
    description="Gita - AI yordamida avtomatik commit yozish CLI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    # GitHub yoki loyiha URL'ini qo‘shing
    url="https://github.com/yourusername/gita",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
