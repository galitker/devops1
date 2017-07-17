from setuptools import setup, find packages


setup(
    name='tryexcept',
    version='0.1',
    description='try_except',
    #url='http://github.com/galitker/devops1/tryexcept.py',
    author='Galit Kerner',
    author_email='galit.cohen.kerner@gmail.com',
    entry_points={
        'console_scripts': [
            'tryexcept=.tryexcept:main',
        ]
    },
    #license='Apache2',
    packages=find_packages(),
    install_requires=requirements,
    zip_safe=False)
