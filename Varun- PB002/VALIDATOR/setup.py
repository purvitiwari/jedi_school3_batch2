from setuptools import setup, find_packages

setup(
    name='validator',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    #py_modules=['wikionterm'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        validator=validator:validate
    ''',
)
