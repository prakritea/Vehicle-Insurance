from setuptools import setup, find_packages

setup(
    name="src",
    version="0.0.1",
    author="Prakriti",
    author_email="prakritisrishti03@gmail.com",  # Update your email
    packages=find_packages(where="src"),  # This will include all packages under 'src'
    package_dir={"": "src"},  # This tells setuptools your code lives in "src"
)
