import re
from setuptools import setup

with open('bfd/__init__.py') as inf:
    match = re.search(r"((\d\.){2,5}\d)", inf.read(), re.MULTILINE)

    if match is None:
        raise RuntimeError('Version could not be found.')

    version = match.groups()[0]

setup(name='PyBFD',
      author='mental',
      url='https://github.com/mental32/PyBFD.py',
      version=version,
      packages=['bfd'],
      license='MIT',
      description='Small async API wrapper for the BFD API',
      include_package_data=True,
      install_requires=requirements,
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
      ]
)
