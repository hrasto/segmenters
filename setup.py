import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="segmenters",
    version="0.1.7",
    author="Rastislav Hronsky",
    author_email="hronskyr@gmail.com",
    description="All kinds of segmenters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hrasto/segmenters",
    project_urls={
        "Bug Tracker": "https://github.com/hrasto/segmenters/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    include_package_data=True,
    package_data={
        "segmenters": ["data/*"],
    },
    install_requires=[
        'pandas',
        'tokenizers',
        'numpy',
        'morfessor'
    ]
)
