from setuptools import setup

setup(
      name="netstorm",
      version="1.0.0",
      url="https://github.com/im-strange/netstorm.git",
      author="im-strange",
      description="DDos with Python and Socket",
      py_modules=["netstorm"],
      install_requires=[
          "socket",
          "threading",
          "random",
          "sys"
      ],
      include_package_data=True,
      packages=[],
      package_data={},
      entry_points={
          "console_scripts": ["netstorm = netstorm:main"]
      }
)
