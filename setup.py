import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pelikan",
    version="0.0.5",
    author="Hakan Ozler",
    author_email="ozler.hakan@gmail.com",
    description="a jupyter notebook tool to make notebooks comment-free",
    long_description=long_description,
    long_description_content_type="text/plain; charset=UTF-8",
    url="https://github.com/ozlerhakan/palikan",
    project_urls={
        "Bug Tracker": "https://github.com/ozlerhakan/pelikan/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    keywords=["python", 'jupyter', 'notebooks'],
    install_requires=[
        'nbconvert>= 6.2.0',
        'nbformat>=5.1.3'
    ],
    entry_points={
        "console_scripts": [
            "pelikan=pelikan.Pelikan:main"
        ],
    }
)
