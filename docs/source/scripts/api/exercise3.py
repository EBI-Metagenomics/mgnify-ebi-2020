#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import csv
from urllib.parse import urlencode

import pandas
from jsonapi_client import Filter, Session
from plotnine import *

API_BASE = "https://www.ebi.ac.uk/metagenomics/api/v1"

RESOURCE = "genomes"

# Filter genomes based on the geopgraphical origin
REGION_FILTERS = {
    "geo_origin": [
        "South America",
        "Africa",
        "Asia",
        "Oceania",
    ]
}

ALL_REGIONS = [
    "Africa",
    "Asia",
    "Europe",
    "North America",
    "Oceania",
    "South America",
]

rows = []

# The next piece of code retrieves the data from the API
with Session(API_BASE) as session:

    filters = Filter(urlencode(REGION_FILTERS, True))

    for genome in session.iterate(RESOURCE, filters):
        for gr_region in genome.geographic_range:
            if genome.num_genomes_total > 1:
                rows.append(
                    {
                        "accession": genome.accession,
                        "geographic_origin": genome.geographic_origin,
                        "geographic_region": gr_region,
                        "geographic_region_rel_abundance": 0,
                    }
                )

    data_frame = pandas.DataFrame(rows)

    # let's get the relative abundance of each region
    for geo_origin, frame in data_frame.groupby("geographic_origin"):
        abundances = data_frame.loc[
            data_frame["geographic_origin"] == geo_origin, "geographic_region"
        ].value_counts(normalize=True)

        for gregion, abundance in abundances.items():
            data_frame.loc[
                (data_frame["geographic_origin"] == geo_origin)
                & (data_frame["geographic_region"] == gregion),
                "geographic_region_rel_abundance",
            ] = (
                abundance * 100
            )

    # remove dups (each region is duplicated now)
    data_frame = data_frame.drop_duplicates(
        subset=["geographic_origin", "geographic_region"], keep="last"
    )

    gb = geom_bar(stat="identity", colour="darkgrey", size=0.3, width=0.6, alpha=0.7)
    gg = (
        ggplot(
            data_frame,
            aes(
                x=data_frame["geographic_origin"],
                y=data_frame["geographic_region_rel_abundance"],
                fill="geographic_region",
            ),
        )
        + gb
        + ggtitle("Geographic range of pan-genome")
        + ylab("Relative abundance (%)")
        + theme(panel_grid_major=element_blank(), panel_grid_minor=element_blank())
        + theme(axis_text_x=element_text(angle=90))
        + theme(axis_title_y=element_text(size=10))
        + theme(axis_text_y=element_text(size=10))
        + theme(axis_title_x=element_blank())
        + theme(axis_text_x=element_text(size=10))
    )

    ggsave(
        filename="genomes_plot.png",
        plot=gg,
        device="png",
        dpi=600,
    )
