******************************
MGnify API data hunt solutions
******************************

Solutions to the questions for the API session `api session`.

Question 1
##########

**Is the number of samples the same as the number of analyses?. What could be the reason?**

Data in MGnify is structured into projects, samples, runs and analyses. Each project contains one or more samples, and each sample can have one or more experiments associated with it (such as metagenomic, amplicon or metatranscriptomic). Analyses are the results obtained from processing a run file (or an assembly derived from the run file) using a given version of the pipeline.

Question 2
##########

**Using the API browser, how many results have been analysed with the pipeline version 4.0 for the OSD study ERP009703?**

You can filter the results using the Filters (select Pipeline 4.0 from the piplines options). Or follow this `https://www.ebi.ac.uk/metagenomics/api/v1/studies/ERP009703/analyses?pipeline_version=4.0 <https://www.ebi.ac.uk/metagenomics/api/v1/studies/ERP009703/analyses?pipeline_version=4.0>`_.

The expected number is: 467, you can get this number from the `meta` section in at the bottom of the JSON result.

Question 3
##########

**What "type" of data is the script downloading?. Which filters are being used to get the filtered data from the API?.**

If you review the code for the script `exercise1.py <https://github.com/EBI-Metagenomics/mgnify-ebi-2020/blob/master/docs/source/scripts/api/exercise1.py>`_ you can spot the endpoint the script is cosuming:

.. code-block:: python

    for sample in session.iterate(
        "biomes/root:Environmental:Aquatic/samples", api_filter
    ):

`"biomes/root:Environmental:Aquatic/samples"` states that the data type is `samples`. You can also check the `type` value on the returned json.

Question 4
##########

**How might you adapt the script to find soil samples taken at the equator?**

The first thing is to find out the biome "code" for soil, you can browse the biomes endopint and use the Filters menu to find it.

After finding it modify the following line in `exercise1.py`_ with:

.. code-block:: python

    for sample in session.iterate(
        "biomes/root:Environmental:Terrestrial:Soil/samples", api_filter
    ):


Question 5
##########

**How many of the OSD2014 samples were taken from the Arctic Ocean?**


You have to modify the `exercise1.py`_ and modify line XX with:

.. code-block:: python

    # configure the filters
    params = {
        "latitude_gte": 70,
        "experiment_type": "metagenomic",
        "ordering": "accession",
        "study_accession": "MGYS00000462"
    }

there are 3 samples from OSD2014 taken from the Artic Ocean.

Question 6 and 7
################

**How similar or different are the phylum compositions of each analysis?. How might you explain any differences?.**
**How many of the analyses look to target bacterial populations and how many are targeting the archaea?**

Some of the analysis target Bacteria and the others to Archea. 3 to Bacteria and 2 to Archea.


Question 8
##########

**How might you adapt the code for the analysis of other studies**

* **perform analysis of taxonomic results bases on the large ribosomal subunit rRNA or the ITS region for fungi?**
* **output the top 20 genera, rather that the top 10?**

To get the results for the LSU rRNA use the endpoint `taxonomy/lsu`, to do this modify the script following this:

.. code-block:: python

    tax_annotations = session.get(
        "/".join(["analyses", analysis_accession, "taxonomy", "lsu"]))

the endpoint is the last bit of that line, the alternatives are:

* ssu
* lsu
* unite (ITS based on Unite)
* itsonedb (ITS based on ITSoneDB)

To include the Top 20 genera or any other taxonomic rank please use `exercise2_question8.py <https://github.com/EBI-Metagenomics/mgnify-ebi-2020/blob/master/docs/source/scripts/api/solutions/exercise2_question8.py>`_.
I've changed the colours on the chart, is for to investigate how to assign the colours you want :).

Question 9
##########

**What type of data can we download using the Toolkit?.**

The toolkit allwos user to download:

* a study metadata using `original_metadata`
* a study analyses files using `bulk_download`
* query MGnify Search service

Question 10
###########

**Based on the files the toolkit has downloaded, how many analyses has the study MGYS00005575?**

The tool will create the following folder structure:

.. code-block:: bash

    MGYS00005575\
        5.0\ => pipeline version

On that you can find all the files for the 2 analyses, if you inspect the files they start with a prefix (`ERZ1303541_XX` and `ERZ1303544_XX`). Those prefixes correspond to analysis.

Question 11
###########

**How could you modify the script `exercise3.py` to download the other functional annotations?**

To download the other functional annotations we have to expand the script. For example, to download the KEGG annotations add the following piece of code

.. code-block:: python

    with open(os.path.join(GENOME_ACCESSION, "API_KEGG_MODULES.csv"), "w") as km_file:
        print("Getting the KEGG modules annotations from the API")
        fields = [
            "name",
            "description",
            "genome-count",
            "pangenome-count",
        ]
        writer = csv.DictWriter(km_file, fieldnames=fields)
        writer.writeheader()
        for kgmodule in session.iterate(RESOURCE + "/" + GENOME_ACCESSION + "/kegg-module"):
            writer.writerow(
                {
                    "name": kgmodule.name,
                    "description": kgmodule.description,
                    "genome-count": kgmodule.genome_count,
                    "pangenome-count": kgmodule.pangenome_count,
                }
            )

Scripts alternatives
####################

You can find alternatives for the `exercise1.py` and for `exercise2.py` in the folder R.

In order to run them you need the `devtools` package to install the `jsonapi` client for R. 
Warning: jsonapi has been deprecated.

.. |info| image:: media/info.png
   :width: 0.26667in
   :height: 0.26667in
.. |action| image:: media/action.png
   :width: 0.26667in
   :height: 0.26667in
.. |question| image:: media/question.png
   :width: 0.26667in
   :height: 0.26667in
