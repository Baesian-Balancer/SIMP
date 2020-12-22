import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SIMP", # Replace with your own username
    version="0.0.1",
    author="Dawson Horvath",
    author_email="horvath.dawson@gmail.com",
    description="monopod models for baesian balancing capstone team 2020.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Baesian-Balancer/SIMP",
    packages=['SIMP'],
    include_package_data=True,    
    install_requires=['pathlib', 'typing'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
