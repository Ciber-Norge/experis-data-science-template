"""
Train a model.
TODO: Add hyper parameters to input or (preferably) file ref with json/yml/whatever that can be
read and sent as dictionary to model)
Argv:
    dataset: Dataset file to use (local file, create/download using pipeline).
             Expects last column to be label and all others to be used as input.
    output-dir: A folder to store any output to
"""
import os
import sys
import argparse
import warnings
from pathlib import Path
import pandas as pd
import xgboost as xgb
import mlflow
import matplotlib as mpl
from IPython.core.display import display, HTML
import json
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import tempfile
from hyperopt import fmin, tpe, hp, SparkTrials, Trials, STATUS_OK
from hyperopt.pyll import scope
import numpy as np

from mlflow.models.signature import infer_signature
import pickle

search_space = {
    "objective": "binary:logistic",  # objective
    "eta": hp.loguniform("learning_rate", -4, -1.2),  # learning rate
    "min_child_weight": hp.loguniform(
        "min_child_weight", -1, 3
    ),  # minimum sum of weights of all observations required in child.
    "max_depth": scope.int(hp.quniform("max_depth", 4, 50, 1)),
    "subsample": hp.loguniform(
        "subsample", -0.91, 0
    ),  # fraction of observations to be randomly samples for each tree.
    "colsample_bytree": hp.loguniform(
        "colsample_bytree", -0.91, 0
    ),  # fraction of columns to be randomly sampled for each tree.
    "colsample_bylevel": hp.loguniform(
        "colsample_bylevel", -0.91, 0
    ),  # subsample ratio of columns for each split, in each level.
    "lambda": hp.loguniform(
        "lambda", -4, 0
    ),  # L2 regularization term on weights (Ridge)
    "alpha": hp.loguniform(
        "alpha", -4, -1.2
    ),  # L1 regularization term on weight (Lasso)
    "gamma": hp.loguniform(
        "gamma", -6, 2.7
    ),  # minimum loss reduction required to make a split
    "seed": 41,
}


def train(search_space, name, dataset):
    """
    Train script with hyperparameters
    """

    def objective(search_space):
        """
        Encapsulated objective-function such that hyperopt function can reach input-data in objective function
        """
        print(X_train.dtypes.value_counts())
        dtrain = xgb.DMatrix(X_train.copy(), label=y_train, enable_categorical=True)
        dtest = xgb.DMatrix(X_test.copy(), label=y_test, enable_categorical=True)
        evallist = [(dtest, "eval"), (dtrain, "train")]


        verbose_eval = 50

        with mlflow.start_run(nested=True):
            search_space["eval_metric"] = ["error", "auc", "logloss"]
            num_round = 1000
            evals_result = {}
            num_features = 80
            bst = xgb.train(
                search_space,
                dtrain,
                num_round,
                evals=evallist,
                evals_result=evals_result,
                early_stopping_rounds=50,
                verbose_eval=verbose_eval,
            )
            print(f"Stopping after {len(evals_result['train']['error'])} rounds")

            min_eval_error = np.min(evals_result["eval"]["error"])
            mlflow.xgboost.log_model(bst, artifact_path="model")

            return {
                "status": STATUS_OK,
                "loss": min_eval_error,
                "booster": bst.attributes(),
            }



    mlflow.set_experiment(name)

    mlflow.xgboost.autolog(
        log_input_examples=False, log_model_signatures=True, log_models=True
    )
    # Load the dataset, split x/y, split train/test
    #df = spark.read.format("delta").load(dataset)
    #df = df.toPandas()

    print(f"Dataset shape: {df.shape}")

    print(f"Dataset shape: {df.shape}")
    # Splitte treningsdatasett i X og y
    X = df.loc[:, ~df.columns.isin(["y"])]
    y = df["y"]

    # dividing X, y into train and test data. Random seed is specified in params dict form jsonfile
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=search_space["seed"]
    )

    # Use dataset shortname in run name along with model type. Better ideas?
    ds_short = Path(dataset).stem

    # -------INIT DONE----
    print("Dataset loaded, split into train test... ready to run hyperoptimalization!")

    with mlflow.start_run(run_name=f"xgb_{ds_short}"):
        best_params = fmin(
            fn=objective,
            space=search_space,
            algo=tpe.suggest,
            max_evals=100,
        )


def main(arguments):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # environment parameters
    parser.add_argument(
        "-n",
        "--name",
        help="name of model experiment for Mlflow trakcing",
        required=True,
    )

    parser.add_argument(
        "-i", "--dataset", help="local path to training dataset", required=True
    )

    parser.add_argument(
        "-c",
        "--cross-val",
        help="Run cross calidation",
        default=False,
        action="store_true",
    )

    # parse the arguments
    args = parser.parse_args(arguments)
    train(search_space, args.name, args.dataset, args.cross_val)


if __name__ == "__main__":
    main(sys.argv[1:])