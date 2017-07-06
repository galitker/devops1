from setuptools import setup, find packages


setup(
    name='tryexcept',
    version='0.1',
    description='try_except',
    url='http://github.com/galitker/try_except',
    author='Galit Kerner',
    author_email='galit.cohen.kerner@gmail.com',
    entry_points={
        'console_scripts': [
            'try_except=home.student.tryexcept:main',
        ]
    },
    #license='Apache2',
    packages=['tryexcept'],
    install_requires=requirements,
    zip_safe=False)
