from setuptools import setup

VERSION = "v1.0.2"

setup(
    name="builder",
    version=VERSION,
    license="Apache License 2.0",
    author="The Open Peer Power Authors",
    author_email="hello@openpeerpower.io",
    url="https://openpeerpower.io/",
    description="Opp.io wheels builder form Open Peer Power.",
    long_description="",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Home Automation"
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
    ],
    keywords=["docker", "openpeerpower", "opp.io"],
    zip_safe=False,
    platforms="any",
    packages=["builder"],
    include_package_data=True,
)
