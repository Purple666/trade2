setup(
    name='trade',
    version='0.0.1',
    description='FX Trade package for Python-Guide.org',
    long_description=readme,
    author='Teruo Kikuchi',
    author_email='salem.lights.7mg@gmail.com',
    url='https://github.com/salem7mg/trade',
    license=license,
    install_requires=['TA-Lib' 'MySQL-python']
    packages=find_packages(exclude=('tests', 'docs'))
    test_suite='tests'
)