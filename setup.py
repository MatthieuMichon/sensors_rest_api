from setuptools import setup

setup(
    name='Sensors REST API',
    version='0.1',
    long_description=__doc__,
    packages=['sensors_rest_api'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
