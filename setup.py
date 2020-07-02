import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="gear-torque-calc",
    version="1.0.1",
    description="Get torque output based on gear sizes",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ncrmro/gear-torque-calc",
    author="Nicholas Romero",
    author_email="ncrmro@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=["gear_torque_calc"],
    include_package_data=True,
    install_requires=[],
    entry_points={},
)
