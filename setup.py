from setuptools import setup

setup(
    name = "lesting.api.client",
    version = "0.1.2-beta",
    description = "Lesting API Client Libraray",
    url = "https://github.com/LESTINGX/API.CLIENT",
    packages = ["lesting.api.client"],
    namespace_packages = ["lesting.api"],
    install_requires = [
        "httplib2"
    ],
    zip_safe = False
)