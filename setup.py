import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SIMP",
    version="0.0.1",
    author="Dawson Horvath",
    author_email="horvath.dawson@gmail.com",
    description="monopod models for baesian balancing capstone team 2020.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Baesian-Balancer/SIMP",
    packages=setuptools.find_packages(),  
    package_data={'gym_ignition_models': [
        'meshes/*.*',
        'meshes/**/*.*',
        'meshes/**/**/*.*',
        '*/meshes/*.*',
        '*/meshes/**/*.*',
        '*/meshes/**/**/*.*',
        '*/*.sdf',
        '*/*.urdf',
        '*/model.config',
    ]},    
    include_package_data=True,  
    install_requires=['pathlib', 'typing'],
    python_requires='>=3.8',
)
