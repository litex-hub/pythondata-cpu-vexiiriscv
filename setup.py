import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

from pythondata_cpu_vexiiriscv import version_str

setuptools.setup(
    name="pythondata-cpu-vexiiriscv",
    version=version_str,
    author="LiteX Authors",
    author_email="litex@googlegroups.com",
    description="""\
Python module containing verilog files for VexiiRiscv cpu.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/litex-hub/pythondata-cpu-vexiiriscv",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    zip_safe=False,
    packages=setuptools.find_packages(),
    package_data={
    	'cpu_vexiiriscv': ['cpu_vexiiriscv/verilog/**'],
    },
    include_package_data=True,
    project_urls={
        "Bug Tracker": "https://github.com/litex-hub/pythondata-cpu-vexiiriscv/issues",
        "Source Code": "https://github.com/litex-hub/pythondata-cpu-vexiiriscv",
    },
)
