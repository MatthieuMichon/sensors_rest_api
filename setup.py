from setuptools import setup

setup(
    name='Sensors REST API',
    version='0.1',
    description='A REST API for retrieving data from sensors',
    packages=['sensors_rest_api'],
    include_package_data=True,
    install_requires=['Flask'],
    test_suite='sensors_rest_api.test'
)
