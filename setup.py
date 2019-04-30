from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="wikidump-infobox-extractor",
    version="1.2.0",
    author="Eric Wiener",
    author_email="ericwiener3@gmail.com",
    description="Wikidump infobox extractor.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EricWiener/wikidump-infobox-extractor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["infodump"],
    entry_points={
        'console_scripts': ['infodump=infodump.command_line:main'],
    }
)
