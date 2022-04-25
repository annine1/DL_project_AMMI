import argparse


args=argparse.Namespace(
    lr = 1e-4,
    batch_size = 8,
    train_size = 0.8,
    path = "./data/Images",   # . means go to the current folder which is the main folder
    metadata = "./data/metadata_ok.csv",
    wd = 0.1
)