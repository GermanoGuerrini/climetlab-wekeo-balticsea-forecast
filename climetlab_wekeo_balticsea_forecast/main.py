#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

import climetlab as cml
from climetlab import Dataset
from climetlab.decorators import normalize

__version__ = "0.1.0"


class Main(Dataset):
    name = "Baltic Sea Biogeochemistry Analysis and Forecast"
    home_page = "https://www.wekeo.eu/data?view=dataset&dataset=EO%3AMO%3ADAT%3ABALTICSEA_ANALYSISFORECAST_BGC_003_007"
    licence = "https://www.copernicus.eu/en/access-data/copyright-and-licences"
    documentation = "-"
    citation = "-"

    # These are the terms of use of the data (not the licence of the plugin)
    terms_of_use = (
        "By downloading data from this dataset, "
        "you agree to the terms and conditions defined at "
        "https://www.copernicus.eu/en/access-data/copyright-and-licence"
        "If you do not agree with such terms, do not download the data. "
    )

    dataset = None

    default_options = {
        "xarray_open_mfdataset_kwargs": {"chunks": "auto", "engine": "netcdf4"}
    }

    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("variable", type=str, multiple=True)
    def __init__(self, area, start, end):
        query = {
            "datasetId": "EO:MO:DAT:BALTICSEA_ANALYSISFORECAST_BGC_003_007:cmems_mod_bal_bgc-pp_anfc_P1D-i_202211",
            "boundingBoxValues": [
                {
                    "name": "bbox",
                    "bbox": [
                        area[1],
                        area[2],
                        area[3],
                        area[0],
                    ],
                }
            ],
            "dateRangeSelectValues": [
                {"name": "time", "start": f"{start}", "end": f"{end}"}
            ],
        }

        self.source = cml.load_source("wekeo", query)
        self._xarray = None

    def _to_xarray(self, **kwargs):
        assert len(self) > 0

        options = {}
        options.update(self.default_options)
        options.update(kwargs)

        if len(self) > 1:
            # In this case self.source is a MultiSource instance
            return [s.to_xarray(**options) for s in self.source.sources]

        return self.source._reader.to_xarray(**options)

    def to_xarray(self, **kwargs):
        if self._xarray is None:
            self._xarray = self._to_xarray(**kwargs)

        return self._xarray
