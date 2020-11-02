#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import csv
from urllib.parse import urlencode
from jsonapi_client import Session, Filter

from plotnine import *
import pandas

"""
Let's explore the COG functional annotations across the genomes
for South America and Africa
"""

# API_BASE = "https://wwwdev.ebi.ac.uk/metagenomics/api/v1"

API_BASE = "http://localhost:8000/v1"

RESOURCE = "genomes"

# Filter genomes based on the geopgraphical origin
region_filters = {
    "geo_origin": [
        "South America",
        "Africa",
    ]
}

# pandas

# The next piece of code retrieves the data from the API
with Session(API_BASE) as session:

    for genome in session.iterate(RESOURCE, Filter(urlencode(region_filters, True))):
        print("\t".join([
            genome.accession,
            genome.geographic_origin,
            genome.traxonomic_lineage
        ]))

