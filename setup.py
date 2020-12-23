from setuptools.command.build_ext import build_ext
from setuptools import setup, find_packages, Extension

class CopyMeshes(Extension):
    extension_name = "CopyMeshes"

    def __init__(self):
        Extension.__init__(self, name=self.extension_name, sources=[])
        
class BuildExtension(build_ext):
    """
    Setuptools build extension handler.
    It processes all the extensions listed in the 'ext_modules' entry.
    """

    # Name of the python package (the name used to import the module)
    PACKAGE_NAME = "SIMP"

    def run(self) -> None:
        if len(self.extensions) != 1 or not isinstance(self.extensions[0], CopyMeshes):
            raise RuntimeError("This class can only build one CopyMeshes object")

        if platform.system() != "Linux":
            raise RuntimeError("Only Linux is currently supported")

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext) -> None:
        if ext.name != CopyMeshes.extension_name:
            print(f"Skipping unsupported extension '{ext.name}'")
            return

        if self.inplace:
            raise RuntimeError("Editable mode is not supported by this project")

        # Get the temporary external build directory
        ext_dir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))

        # Package directory
        pkg_dir = os.path.join(ext_dir, self.PACKAGE_NAME)

        # Check that the directory exists
        if not os.path.isdir(pkg_dir):
            raise RuntimeError(f"The build package directory '{pkg_dir}' does not exist")


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="SIMP",
    version="0.0.1",
    author="Dawson Horvath",
    author_email="horvath.dawson@gmail.com",
    description="monopod models for baesian balancing capstone team 2020.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Baesian-Balancer/SIMP",
    packages=find_packages(),  
    package_data={'SIMP': [
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
    install_requires=['pathlib', 'typing', 'setuptools_scm'],
    ext_modules=[CopyMeshes()],
    cmdclass=dict(build_ext=BuildExtension),
    python_requires='>=3.8',
)
