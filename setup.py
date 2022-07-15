extra_kwargs = {}
from setuptools import setup

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
      test_suite='ropemodetest',
      requires=['rope (>= 0.9.4)'],
      install_requires='rope >= 0.9.4'
)

