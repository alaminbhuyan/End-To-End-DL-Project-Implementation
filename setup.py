import setuptools

# Read the readme file
with open(file="README.md", mode="r", encoding="utf-8") as f:
    long_description = f.read()


# Specify the version
__version__ = "0.0.0"

# Add some information about the project
REPO_NAME = "End-To-End-DL-Project-Implementation"
AUTHOR_USER_NAME = "alaminbhuyan"
SRC_REPO = "End-To-End-DL-Project-Implementation"
AUTHOR_EMAIL = "alaminbhuyan321@gmail.com"

# Add setup configuration
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
