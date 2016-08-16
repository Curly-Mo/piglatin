from setuptools import setup
import os


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name='piglatin_microservice',
    version='0.0.1',
    url='https://github.com/Curly-Mo/piglatin',
    license='MIT',
    author='Colin Fahy',
    author_email='colin@cfahy.com',
    packages=['piglatin_microservice', ],
    install_requires=[
        'Flask>=0.11.1',
        'Flask_Cache',
        'Flask-Script',
        'nltk',
    ],
    extras_require={
        'test': ['mock'],
    },
    long_description=read('README.md'),
    description='Pig Latin MicroService Project',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Vicarious',
      'License :: OSI Approved :: MIT License',
    ]
)
