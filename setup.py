import setuptools

# Read the contents of README.md for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pypdfzipcrack',
    version='1.0',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'PyPDF2',
        'pyzipper',
    ],
    entry_points={
        'console_scripts': [
            'pdfzipcrack=pypdfzipcrack.pdfzipcrack:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    description="A tool to crack encrypted PDF and ZIP files.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Specify that README is in Markdown format
)
