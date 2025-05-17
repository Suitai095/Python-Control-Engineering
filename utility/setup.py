from setuptools import setup


def get_requirements_from_file() -> list[str]:
    with open('requirements.txt', 'r') as f:
        requirements = f.read().splitlines()
    return requirements


setup(
    name='calculator',
    version='0.1.0',
    author='Suitai-095',
    install_requires=get_requirements_from_file(),
    package_dir={'': 'src'},
)
