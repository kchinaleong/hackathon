from setuptools import setup

setup(
    name='FlaskApp',
    version='1.0dev',
    long_description=__doc__,
    packages=['flaskapp'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
