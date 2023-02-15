{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

# Table of Contents
- [{{cookiecutter.project\_name}}](#cookiecutterproject_name)
- [Table of Contents](#table-of-contents)
- [How to use this template](#how-to-use-this-template)
    - [Template development environment](#template-development-environment)
      - [Install virtualenv](#install-virtualenv)
      - [Setup using](#setup-using)
      - [Activate environment](#activate-environment)
      - [Install Dependencies](#install-dependencies)
  - [Develop in the template](#develop-in-the-template)
      - [Testing](#testing)
      - [Linting](#linting)
  - [Project Organization](#project-organization)


# How to use this template

### Template development environment
To develop in the template, you need to setup a virtual environment. This is done using the following steps:

#### Install virtualenv
````
python3 -m pip install virtualenv
````

#### Setup using
```
cd data-science-template
python -m venv dst-env
```

#### Activate environment
Max / Linux
```
source dst-env/bin/activate
```

Windows
```
dst-env\Scripts\activate
```

#### Install Dependencies
```
pip install -r requirements.txt
```

## Develop in the template
```
python -m pip install -e .
```    
#### Testing
To run the template tests, install pytest using pip or conda and then from the repository root run
 
    pytest tests

#### Linting
To verify that your code adheres to python standards run linting as shown below:

    flake8 --max-line-length=120 *.py hooks/ tests/
Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
