from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


with open("README.rst") as f:
    readme = f.read()


setup(
    name="musixmatch-py",
    author="sarzz2",
    url="https://github.com/takos22/codingame",
    project_urls={},
    version="0.1",
    packages=["musixmatch-py"],
    license="MIT",
    description="Pythonic wrapper for the undocumented musixmatch API.",
    long_description=readme,
    long_description_content_type="text/x-rst",
    install_requires=requirements,
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
