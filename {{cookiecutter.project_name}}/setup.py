from setuptools import (
    setup,
)

setup(
    name="{{cookiecutter.project_name}}",
    author='{{cookiecutter.author}}',
    url=""
    version="1.0",
    description="{{cookiecutter.project_name}}, {{cookiecutter.description}}",
    packages=[
        "{{cookiecutter.PROJECT_NAME|lower}}"
    ],
    package_dir={
        "{{cookiecutter.PROJECT_NAME|lower}}": "{{cookiecutter.PROJECT_NAME|lower}}",
    },
    include_package_data=True,
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "",
        ]
    },
)