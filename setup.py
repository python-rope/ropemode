# dependencies for python 2 or python 3
import sys
if sys.version < '3':
    requires = ['rope (>= 0.9.4)']
    install_requires = ['rope >= 0.9.4']
else:
    requires = ['rope_py3k (>= 0.9.4)']
    install_requires = ['rope_py3k >= 0.9.4']


extra_kwargs = {}
try:
    from setuptools import setup
    extra_kwargs['install_requires'] = install_requires
except ImportError:
    from distutils.core import setup


def get_something_from_file(thing):
    # get information from __init__.py file
    # before module is installed.

    fname = 'ropemode/__init__.py'
    with open(fname) as f:
        fcontent = f.readlines()
    thing_line = [l for l in fcontent if thing in l][0]
    return thing_line.split('=')[1].strip().strip("'").strip('"')

VERSION = get_something_from_file('VERSION')
INFO = get_something_from_file('INFO')


classifiers=[
    'Development Status :: 4 - Beta',
    'Operating System :: OS Independent',
    'Environment :: X11 Applications',
    'Environment :: Win32 (MS Windows)',
    'Environment :: MacOS X',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development']

setup(name='ropemode',
      version=VERSION,
      description=INFO,
      author='Ali Gholami Rudi',
      author_email='aligrudi@users.sourceforge.net',
      url='http://rope.sf.net/',
      packages=['ropemode'],
      license='GNU GPL',
      classifiers=classifiers,
      requires=requires,
      use_2to3=True,
      **extra_kwargs
)

