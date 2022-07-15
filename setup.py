from setuptools import find_packages, setup

setup(
    name="ropemode",
    version="0.5",
    description="a helper for using rope refactoring library in IDEs",
    author="Ali Gholami Rudi",
    author_email="aligrudi@users.sourceforge.net",
    url="http://rope.sf.net/",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    license="GNU GPL",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Environment :: X11 Applications",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
    install_requires=["rope >= 0.9.4"],
)
