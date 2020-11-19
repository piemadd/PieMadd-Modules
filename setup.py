from setuptools import find_packages, setup
setup(
    name='piemadd-modules',
    packages=find_packages(include=['piemadd-modules']),
    version='0.1.0',
    description='Modules for easy and scalable web servers.',
    authors=["Piero Maddaleni"],
    license='Apache-2.0',
	install_requires=[],
    setup_requires=['pytest-runner'],
)