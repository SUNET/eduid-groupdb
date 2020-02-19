import os
from setuptools import setup, find_packages

version = '0.0.1'

here = os.path.abspath(os.path.dirname(__file__))

install_requires = [x for x in open(os.path.join(here, 'requirements.txt')).read().split('\n') if len(x) > 0]
testing_extras = [x for x in open(os.path.join(here, 'test_requirements.txt')).read().split('\n')
                  if len(x) > 0 and not x.startswith('-')]

setup(
    name='eduid-groupdb',
    version=version,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['eduid_groupdb'],
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
    tests_require=testing_extras,
    url='https://github.com/SUNET/eduid-groupdb',
    license='BSD-2-Clause',
    author='Johan Lundberg',
    author_email='lundberg@sunet.se',
    description='Group operations for Neo4j'
)
