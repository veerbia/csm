from setuptools import setup, find_packages

setup(
    name="csm",
    version="0.1",
    py_modules=["generator", "models", "watermarking"],
    packages=find_packages(),
    install_requires=[
        "torch",
        "torchvision",
        "numpy",
        "matplotlib",
        "scipy",
        "scikit-learn",
        "pandas",
    ],
)
