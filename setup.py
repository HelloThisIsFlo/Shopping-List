from setuptools import setup
from os.path import expanduser

HOME = expanduser("~")

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='shoppinglist',
    version='1.0.3',
    description='Quickly different combinations of prices and spare money',
    long_description=readme(),
    keywords='shopping calculator cost saving money shopping_list cli awesome',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
        'Topic :: Office/Business :: Financial',
        'Topic :: Home Automation'
    ],
    url='https://floriankempenich.github.io/Shopping-List',
    author='Florian Kempenich',
    author_email='Flori@nKempenich.com',
    packages=['shoppinglist'],
    license='MIT',
    scripts=['bin/shoppinglist'],
    install_requires=[
        'click',
        'pyyaml'
    ],
    include_package_data=True,
    zip_safe=True
)
