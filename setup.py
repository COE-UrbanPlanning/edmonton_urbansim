from setuptools import setup, find_packages

setup(
    name='baus',
    version='0.1dev',
    description='Edmonton UrbanSim.',
    author='GeoDesign',
    license='COE',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: COE License'
    ],
    packages=find_packages(exclude=['*.tests']),
    install_requires=[
        'boto'
    ]
)
