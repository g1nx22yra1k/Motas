"""
Setup script for Motas
"""

from setuptools import setup, find_packages

setup(
    name="motas",
    version="0.1.0",
    author="g1nx22yra1k",
    description="A simple and efficient task management system",
    url="https://github.com/g1nx22yra1k/Motas",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "motas=src.cli:main",
        ],
    },
    keywords="task management, productivity, cli, todo",
)
