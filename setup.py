from setuptools import find_packages, setup


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="packagemaker",
    version="0.0.10",
    description="pip code to install package from github",
    package_dir={"": "src"},
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Dipson",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=['pyperclip'],
    python_requires=">=3.10",
)

#packages=["pipfromgit"], packages=find_packages("github"),
