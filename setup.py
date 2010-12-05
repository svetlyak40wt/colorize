from setuptools import setup

setup(
    name = 'colorizer',
    version = '0.1.2',
    description = 'Console colorizer, which acts like grep but paint each match in it\'s own color.',
    author = 'Alexander Artemenko',
    author_email = 'svetlyak.40wt@gmail.com',
    url = 'http://github.com/svetlyak40wt/colorizer/',
    license = 'New BSD License',
    install_requires = ['termcolor'],
    classifiers = [
        'Environment :: Console',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python',
    ],
    entry_points = """
    [console_scripts]
    colorize = colorizer:main
    """,
)
