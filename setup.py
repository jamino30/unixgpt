from setuptools import setup, find_packages

from unixgpt.constants import VERSION

# dependencies
REQUIREMENTS = [
    "openai==0.28.1",
    "pyperclip==1.8.2",
    "rich==13.6.0",
]

setup(
    name="unixgpt",
    version=VERSION,
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    entry_points={
        "console_scripts": [
            "unixgpt = unixgpt.__main__:main"
        ]
    },
    description="unixgpt is a powerful bridge between natural language and UNIX commands",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
