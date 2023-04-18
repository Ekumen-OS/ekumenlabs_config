# ekumenlabs_config

[![tests](https://github.com/Ekumen-OS/ekumenlabs_config/actions/workflows/tests.yaml/badge.svg)](https://github.com/Ekumen-OS/ekumenlabs_config/actions/workflows/tests.yaml)
[![codecov](https://codecov.io/gh/Ekumen-OS/ekumenlabs_config/branch/main/graph/badge.svg?token=mRGjPkrBjt)](https://codecov.io/gh/Ekumen-OS/ekumenlabs_config)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![poetry-managed](https://img.shields.io/badge/poetry-managed-blueviolet)](https://python-poetry.org)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ekumenlabs_config)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/ekumenlabs_config)
[![PyPI](https://img.shields.io/pypi/v/ekumenlabs_config?logo=python)](https://pypi.org/project/ekumenlabs_config/)


This is a very simple project to use/store configurations persisted in a database (accessed via tortoise-orm).


### Examples


```python
from ekumenlabs_config import get_bool_config


async def do_something():
    if await get_bool_config("simple.example"):
        print("Yes, it is simple!")

```


## Installation

### Pip

`pip install ekumenlabs_config`

### Pipenv

`pipenv install ekumenlabs_config`

### Poetry

`poetry add ekumenlabs_config`

### PDM

`pdm add ekumenlabs_config`

## Notes for maintainers

### Release

To create a new release, create a github release and a github action will take care of building and publishing. After
that, there will be a PR automatically created to bump the version in `main`.
