from setuptools import setup, find_packages
setup_args=dict(
    name="PySCli",
    version="1.0",
    author="Sancho Godinho",
    description="A Simple Module to Get User Terminal Commands...\nSee https://github.com/sancho1952007/PySCLI",
    packages=['pyscli'],
    keywords=['cli()']
    )
install_requires=[]

if __name__=='__main__':
    setup(**setup_args, install_requires=install_requires)
