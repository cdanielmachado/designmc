[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![PyPI version](https://badge.fury.io/py/designmc.svg)](https://badge.fury.io/py/designmc)
[![Build Status](https://travis-ci.com/cdanielmachado/designmc.svg?branch=master)](https://travis-ci.com/cdanielmachado/designmc)

![DesignMC](logo_300px.png)


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
![](data:image/jpeg;base64,WyFbTGljZW5zZV0oaHR0cHM6Ly9pbWcuc2hpZWxkcy5pby9iYWRnZS9MaWNlbnNlLUFwYWNoZSUyMDIuMC1ibHVlLnN2ZyldKGh0dHBzOi8vb3BlbnNvdXJjZS5vcmcvbGljZW5zZXMvQXBhY2hlLTIuMCkKWyFbUHlQSSB2ZXJzaW9uXShodHRwczovL2JhZGdlLmZ1cnkuaW8vcHkvaGlvcmNvLnN2ZyldKGh0dHBzOi8vYmFkZ2UuZnVyeS5pby9weS9oaW9yY28pCgojIEhpT3JDbwoKQ29tcHV0aW5nICoqSGkqKmdoZXItKipPcioqZGVyICoqQ28qKi1vY2N1cnJlbmNlIHBhdHRlcm5zIGluIG1pY3JvYmlhbCBzYW1wbGVzLgoKIyMjIEluc3RhbGxhdGlvbgoKQ2FuIGJlIGVhc2lseSBpbnN0YWxsZWQgdXNpbmcgKipwaXAqKjoKCmBgYApwaXAgaW5zdGFsbCBoaW9yY28KYGBgCgoKIyMjIFVzYWdlCgpBcyBzaW1wbGUgYXM6CgpgYGAKaGlvcmNvIHNhbXBsZXMudHN2CmBgYAoKWW91IGNhbiBkb3dubG9hZCBvdXIgZXhhbXBsZSBoZXJlOiBbc2FtcGxlcy50c3ZdKGh0dHBzOi8vZ2l0aHViLmNvbS9jZGFuaWVsbWFjaGFkby9IaU9yQ28vcmF3L21hc3Rlci9leGFtcGxlL3NhbXBsZXMudHN2KSAoZGF0YSBmcm9tIHRoZSBIb21lIE1pY3JvYmlvbWUgUHJvamVjdCksIGFuZCBjaGVjayB0aGUgZG9jdW1lbnRhdGlvbiBmb3IgbW9yZSBvcHRpb25zIGFuZCBkZXRhaWxzOgoKYGBgCmhpb3JjbyAtaApgYGAKCiMjIyBDcmVkaXRzCgpEYW5pZWwgTWFjaGFkbywKRXVyb3BlYW4gTW9sZWN1bGFyIEJpb2xvZ3kgTGFib3JhdG9yeSAoRU1CTCksCjIwMTkK)