
![Header Image](resources/experis_logo.png)

# Cookiecutter for Experis Data Science Template


This Project is forked from [cookiecutter-data-science](http://drivendata.github.io/cookiecutter-data-science/) and heavily modified to fit the needs of Experis Data Science projects. The original project is a great starting point for Data Science projects and we encourage you to use it. 

This template is also heabily inspired from [Equinors´s Data Science template ](https://github.com/equinor/data-science-template)


## Contribute
If you want to contirbute to this template or have any suggestions, please create an issue or a pull request at the [Experis Project homepage](https://github.com/Ciber-Norge/experis-data-science-template)


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

One of the following:
``` bash
$ pip install cookiecutter
$ pip3 install cookiecutter
$ python3 -m pip3 install cookiecutter


```


or with conda:

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://github.com/Ciber-Norge/experis-data-science-template.git

[![asciicast](https://asciinema.org/a/244658.svg)](https://asciinema.org/a/244658)


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── .gitignore               <- Files that should be ignored by git. Add seperate .gitignore files in sub folders if 
│                               needed
├── conda_env.yml            <- Conda environment definition for ensuring consistent setup across environments
├── LICENSE
├── README.md                <- The top-level README for developers using this project.
├── requirements.txt         <- The requirements file for reproducing the analysis environment, e.g.
│                               generated with `pip freeze > requirements.txt`. Might not be needed if using conda.
├── setup.py                 <- Metadata about your project for easy distribution.
│
├── data
│   ├── interim_[desc]       <- Interim files - give these folders whatever name makes sense.
│   ├── processed            <- The final, canonical data sets for modeling.
│   ├── raw                  <- The original, immutable data dump.
│   ├── temp                 <- Temporary files.
│   └── training             <- Files relating to the training process
│
├── docs                     <- Documentation
│   ├── data_science_code_of_conduct.md  <- Code of conduct.
│   ├── process_documentation.md         <- Standard template for documenting process and decisions.
│   └── writeup              <- Sphinx project for project writeup including auto generated API.
│      ├── conf.py           <- Sphinx configurtation file.
│      ├── index.rst         <- Start page.
│      ├── make.bat          <- For generating documentation (Windows)
│      └── Makefikle         <- For generating documentation (make)
│
├── examples                 <- Add folders as needed e.g. examples, eda, use case
│
├── extras                   <- Miscellaneous extras.
│   └── add_explorer_context_shortcuts.reg    <- Adds additional Windows Explorer context menus for starting jupyter.
│
├── notebooks                <- Notebooks for analysis and testing
│   ├── eda                  <- Notebooks for EDA
│   │   └── example.ipynb    <- Example python notebook
│   ├── features             <- Notebooks for generating and analysing features (1 per feature)
│   ├── modelling            <- Notebooks for modelling
│   └── preprocessing        <- Notebooks for Preprocessing 
│
├── scripts                  <- Standalone scripts
│   ├── deploy               <- MLOps scripts for deployment (WIP)
│   │   └── score.py         <- Scoring script
│   ├── train                <- MLOps scripts for training
│   │   ├── submit-train.py  <- Script for submitting a training run to Azure ML Service
│   │   ├── submit-train-local.py <- Script for local training using Azure ML
│   │   └── train.py         <- Example training script using the iris dataset
│   ├── example.py           <- Example sctipt
│   └── MLOps.ipynb          <- End to end MLOps example (To be refactored into the above)
│
├── src                      <- Code for use in this project.
│   └── {{cookiecutter.package_name}}       <- Example python package - place shared code in such a package
│       ├── __init__.py      <- Python package initialisation
│       ├── examplemodule.py <- Example module with functions and naming / commenting best practices
│       ├── features.py      <- Feature engineering functionality
│       ├── io.py            <- IO functionality
│       └── pipeline.py      <- Pipeline functionality
│
└── tests                    <- Test cases (named after module)
    ├── test_notebook.py     <- Example testing that Jupyter notebooks run without errors
    └── {{cookiecutter.package_name}}       <- {{cookiecutter.package_name}} tests
        ├── examplemodule    <- examplemodule tests (1 file per method tested)
        ├── features         <- features tests
        ├── io               <- io tests
        └── pipeline         <- pipeline tests
```


### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    pytest tests
