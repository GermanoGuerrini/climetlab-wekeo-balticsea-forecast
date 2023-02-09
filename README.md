## climetlab-wekeo_balticsea_forecast

A dataset plugin for climetlab for the dataset wekeo-balticsea-forecast-main.


Features
--------

In this README is a description of how to get the dataset(s) provided by the python package wekeo_balticsea_forecast.

## Datasets description

There are two datasets: 

### 1 : `main`
TODO: write documentation.


### 2 : TODO
No second dataset yet.


## Using climetlab to access the data

See the [demo notebooks](https://github.com/GermanoGuerrini/climetlab-wekeo-balticsea-forecast/tree/main/notebooks)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GermanoGuerrini/climetlab-wekeo-balticsea-forecast/main?urlpath=lab)


- [demo_main.ipynb](https://github.com/GermanoGuerrini/climetlab-wekeo-balticsea-forecast/tree/main/notebooks/demo_main.ipynb)
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/GermanoGuerrini/climetlab-wekeo-balticsea-forecast/blob/main/notebooks/demo_main.ipynb) 
[![Open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GermanoGuerrini/climetlab-wekeo-balticsea-forecast/blob/main/notebooks/demo_main.ipynb) 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GermanoGuerrini/climetlab-wekeo-balticsea-forecast/main?filepath=notebooks/demo_main.ipynb)
[<img src="https://deepnote.com/buttons/launch-in-deepnote-small.svg">](https://deepnote.com/launch?name=MyProject&url=https://github.com/GermanoGuerrini/climetlab-wekeo-balticsea-forecast/tree/main/notebooks/demo_main.ipynb)


- TODO.


The climetlab python package allows easy access to the data with a few lines of code such as:
``` python

!pip install climetlab climetlab-wekeo-balticsea-forecast
import climetlab as cml
ds = cml.load_dataset("wekeo-balticsea-forecast", area=[60, 16, 55, 22], start="20201002", end="20201003", variable="depth")
ds.to_xarray()
```


Support and contributing
------------------------

Either open a issue on github if this is a github repository, or send an email to email@example.com.

LICENSE
-------

See the LICENSE file.
(C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
This software is licensed under the terms of the Apache Licence Version 2.0
which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
In applying this licence, ECMWF does not waive the privileges and immunities
granted to it by virtue of its status as an intergovernmental organisation
nor does it submit to any jurisdiction.

Authors
-------

Germano Guerrini and al.

See also the CONTRIBUTORS.md file.
