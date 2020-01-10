[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![PyPI version](https://badge.fury.io/py/designmc.svg)](https://badge.fury.io/py/designmc)

# DesignMC

Designing microbial communities using genome-scale metabolic models.


### Installation

Can be easily installed using **pip**:

```
pip install designmc
```

### Usage

**DesignMC** is a tool for designing synthetic microbial communities with a desired phenotypic trait (i.e. design target) using genome-scale metabolic models. The minimum required input is a list of single-species models, one design target (secreted metabolite), and a definition of the growth medium:

```
designmc models/*.xml -t trp__L -m M9 -d mediadb.tsv
```

> **Please note** that this tool is still under development. It currently only supports models using [BiGG](http://bigg.ucsd.edu/) notation, such as those created with [CarveMe](https://github.com/cdanielmachado/carveme). The only design strategy currently available is random sampling. 
 
You can control the maximum number of species per community (example: `-s 5` or `--species 5 `) and the maximum number of combinations to simulate (`-n 100` or `--iters 100`).

For more options and details please check the help menu:

```
designmc -h
```

### Credits

Daniel Machado,
European Molecular Biology Laboratory (EMBL),
2020
