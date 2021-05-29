from setuptools import setup

with open("README.rst") as f:
    readme = f.read()


setup(
    name="musixmatch-py",
    author="sarzz2",
    url="https://github.com/sarzz2/musixmatch-py",
    project_urls={
        "Documentation": "https://musixmatch-py.readthedocs.io/en/latest/",
    },
    version="0.2",
    packages=["musixmatch"],
    license="MIT",
    description="Pythonic wrapper for the undocumented musixmatch API.",
    long_description=readme,
    long_description_content_type="text/x-rst",
    install_requires="requests",
    python_requires=">=3.6",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
