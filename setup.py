import sys

if sys.version < '3':
    rope_package = 'rope'
else:
    rope_package = 'rope_py3k'

extra_kwargs = {}
try:
    from setuptools import setup
    extra_kwargs['install_requires'] = [
        'future >= 0.11.2',
        rope_package + ' >= 0.9.4'
    ]
except ImportError:
    from distutils.core import setup

import ropemode


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
    'Topic :: Software Development']

setup(name='ropemode',
      version=ropemode.VERSION,
      description=ropemode.INFO,
      author='Ali Gholami Rudi',
      author_email='aligrudi@users.sourceforge.net',
      url='http://rope.sf.net/',
      packages=['ropemode'],
      license='GNU GPL',
      classifiers=classifiers,
      requires=['future (>= 0.11.2)', rope_package + ' (>= 0.9.4)'],
      **extra_kwargs
)
