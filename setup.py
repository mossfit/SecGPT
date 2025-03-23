from setuptools import setup, find_packages

setup(
    name="SecGPT",
    version="0.1.0",
    description="AI Assisted Security Tool for vulnerability scanning and recommendations.",
    author="Mainak Basak",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'secgpt = secgpt.cli:main',
        ],
    },
)
