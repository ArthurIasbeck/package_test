from setuptools import setup, find_packages

setup(
    name="MyPackage",
    version="0.1",
    packages=find_packages(),
    description="A brief description of MyPackage.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/mypackage",  # Optional
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
