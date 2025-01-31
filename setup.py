from setuptools import setup, find_packages

setup(
    name="medical_data_warehouse",
    version="0.1",
    description="A project for scraping, processing, and storing medical business data from Telegram.",
    author="Nebiyou Abebe",
    author_email="nebamagna@gmail.com",
    packages=find_packages(where="src"),  # Find packages in the `src` directory
    package_dir={"": "src"},  # Specify that packages are located under `src`
    install_requires=[
        # Add your project dependencies here
        "requests",
        "pandas",
        "fastapi",
        "uvicorn",
    ],
    python_requires=">=3.8",
    include_package_data=True,  # Include non-Python files (e.g., data files)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)