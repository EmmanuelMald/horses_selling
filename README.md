# Horse Selling Pipeline
This repo contains a data ingestion pipeline to extract information from a text, and set some data into different forms for selling.

## How to Run this repo

### 1.- Install uv - An extremely fast Python package and project manager, written in Rust.

You can install it following the instructions from its [**GitHub Repository**](https://github.com/astral-sh/uv)

### 2.- Sync the project dependencies

After installing uv CLI (Command Line Interface), in the terminal execute:

    uv sync

This will update the project’s environment


### 3. Install *make* (optional)

Make is used to compile and build projects and automating a wide variety of repetitive tasks.

You can download it [**here**](https://gnuwin32.sourceforge.net/packages/make.htm)

## Repo Structure

This repo has the next structure:

- app/: Contains all the files related to the deployment

- horses_selling/: It has the core of this application, it has the configuration files and useful functions.

- notebooks/: It has all the testing code. Whenever we want to test a new feature/functionality, we should first create a notebook, make all the necessary tests, and when we get something working, then we move that code to a python script 

- docs/: markdown files that builds the project documentation

- mkdocs.yml: Tree of the documentation files

- uv.lock & pyproject.toml: Dependency manager tool