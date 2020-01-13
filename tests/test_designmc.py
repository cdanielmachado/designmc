#!/usr/bin/env python

"""Tests for `designmc` package."""

import unittest
from designmc.designmc import design
from designmc.cli import extract_id_from_filepath
from reframed import Environment, ModelCache
from glob import glob
import pandas as pd

TARGET = 'R_EX_M_succ_e'
SIZE = 2
ITERS = 100
GROWTH = 0.1
C6_THRESH = 30
AA_THRESH = 10

FOLDER = "tests/data/"
#FOLDER = "data/"
MEDIADB = FOLDER + "media_db.tsv"
MODELS = FOLDER + "*.xml"


class TestDesignMC(unittest.TestCase):

    def setUp(self):
        self.media_db = pd.read_csv(MEDIADB, sep="\t")
        models = glob(MODELS)
        self.species = [extract_id_from_filepath(model) for model in models]
        self.cache = ModelCache(self.species, models)

    def test_on_C6(self):
        cpds = self.media_db.query("medium == 'C6'")["compound"]
        env = Environment.from_compounds(cpds, fmt_func=lambda x: f"R_EX_M_{x}_e")
        df = design(self.species, TARGET, env, size=SIZE, iters=ITERS, growth=GROWTH, modelcache=self.cache)
        self.assertGreater(df.shape[0], 1)
        self.assertGreater(df["value"].max(), C6_THRESH)

    def test_on_AA(self):
        cpds = self.media_db.query("medium == 'AA'")["compound"]
        env = Environment.from_compounds(cpds, fmt_func=lambda x: f"R_EX_M_{x}_e")
        df = design(self.species, TARGET, env, size=SIZE, iters=ITERS, growth=GROWTH, modelcache=self.cache)
        self.assertGreater(df.shape[0], 1)
        self.assertGreater(df["value"].max(), AA_THRESH)


