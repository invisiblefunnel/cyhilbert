from setuptools import setup, Extension


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="cyhilbert",
    version="1.1.0",
    author="Danny Whalen",
    author_email="daniel.r.whalen@gmail.com",
    url="https://github.com/invisiblefunnel/cyhilbert",
    license="MIT",
    license_files=["LICENSE"],
    description="A cythonized version of that one hilbert function you keep copy-pasting.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    extras_require={"tests": ["hilbertcurve"]},
    python_requires=">=3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    ext_modules=[Extension("cyhilbert", ["src/cyhilbert/cyhilbert.c"])],
)
