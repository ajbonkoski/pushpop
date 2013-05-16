from setuptools import setup

setup(name='pushpo',
      version='1.0',
      description='A very simple stack-based VM',
      url='https://bitbucket.org/abonkosk/pushpop',
      author='Anthony J Bonkoski',
      author_email='ajbonkoski@gmail.com',
      packages=['pushpop'],
      scripts=['bin/pushpop'],
      zip_safe=False)
