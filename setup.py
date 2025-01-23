from setuptools import setup, find_packages

# Define constants
__version__ = "0.0.0"
REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "eliabujohnmpuya"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "eliabujohnmpuya@gmail.com"

# Read the long description from README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Setup configuration
setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for an NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},  # 'src' is the base directory for packages
    packages=find_packages(where="src"),  # Automatically find packages in 'src'
    install_requires=[
        "transformers",
        "datasets",
        "torch",
        "nltk",
        "pandas",
        # Add other dependencies here
    ],
    python_requires=">=3.6",  # Specify the minimum Python version
)
