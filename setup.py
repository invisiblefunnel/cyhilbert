from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="cyhilbert",
    version="1.3.0",
    author="Danny Whalen",
    author_email="daniel.r.whalen@gmail.com",
    url="https://github.com/invisiblefunnel/cyhilbert",
    packages=find_packages(),
    license="MIT",
    license_files=["LICENSE"],
    description="A cythonized version of that one hilbert function you keep copy-pasting.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    extras_require={"tests": ["mypy", "hilbertcurve"]},
    python_requires=">=3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    ext_modules=cythonize(
        [Extension("hilbert", ["cyhilbert/hilbert.pyx"])],
        compiler_directives={
            "language_level": 3,
            "embedsignature": True,
        },
    ),
    package_data={"cyhilbert": ["__init__.pyi", "py.typed"]},
)
