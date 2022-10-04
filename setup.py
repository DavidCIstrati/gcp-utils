import setuptools

setuptools.setup(
    name="gcp_utils",
    zip_safe=False,
    version="0.0.1",
    author="David Istrati",
    author_email="dcistr26@colby.edu",
    description="Utilities for GCP",
    url="https://github.com/DavidCIstrati/gcp_utils",
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    python_requires=">=3.7",
)
