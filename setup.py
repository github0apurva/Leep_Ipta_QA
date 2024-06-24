import setuptools

with open("README.md", "r", encoding = "utf-8" ) as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Leep_Ipta_QA"
AUTHOR_USER_NAME = "github0apurva"
SRC_REPO = "IPTA_QA"
AUTHOR_EMAIL = "apurva.c27@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description = "Question answering system for Iptacopan",
    long_description=long_description,
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {"Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
                    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where = "src")
)