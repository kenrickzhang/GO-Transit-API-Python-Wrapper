from setuptools import setup, find_packages

setup(
    name="gotransit",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=["requests", "python-dotenv"],
)
