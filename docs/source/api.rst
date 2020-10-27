********************
MGnify API data hunt
********************

This tutorial provides an introduction to the API (Application Programming Interface) and tools & methods 
that can be used to access microbiome data programmatically from MGnify. You will learn about the structure 
of the API and the data, as well as how to write scripts to analyze data programmatically.

Learning objectives
^^^^^^^^^^^^^^^^^^^

- Understand how to access data using MGnify API
- Understand how to filter data sets using metadata
- Learn how to write scripts to programmatically access to the data

Prerequisites
-------------

For this tutorial you will need a working directory to store that data .. important:: 

...code-block:: bash
    mkdir -p ~/Mgnify2020/session_api/
    export DATA_DIR=~/Mgnify2020/session_api/


You will also need the dependencies, we will install them using miniconda.

...code-block:: bash
    conda create -n mgnify-api python=3.8

    conda activate mgnify-api

    pip install pandas numpy scipy plotnine jsonapi-client

We are using miniconda to create a virtual in


An introduction to MGnify REST API
----------------------------------

MGnify is a freely avaiable hub for the analysis and exploration of metagenomic, metatranscriptomic,
amplicon and assembled datasets. The resource provides rich functional and taxonomic analyses of
user-submitted sequences, as well as analysis of publicly avaiable metagenomic datasets drawn
from the European Nucleotide Archive (ENA).


How to browse data using MGnify REST API
----------------------------------------

The MGnify REST API allows retrieval of over 400.000 (and counting) publicy
avaiable metagenomics, metatranscriptomic, amplicon and assembly datasets,
sampled from diverse environments.

The base URL to the API is: https://www.ebi.ac.uk/metagenomics/api

The API documentation at: https://www.ebi.ac.uk/metagenomics/api/docs

|api_overview|\
**Figure 1**: MGnify API browser.

The base URL provides access to several resource collections, such as *studies*
**samples**, **runs**, **analyses**, **genomes**, **biomes** and **experiment-types**

|action|\  Open https://www.ebi.ac.uk/metagenomics/api/latest/studies in your browser. This will a paginated list of all of the publicy available studies. Now open the list of samples using: https://www.ebi.ac.uk/metagenomics/api/latest/samples


|question|\  What kind of experiment types can be found in MGnify?. Hint: follow the relavant link on: https://www.ebi.ac.uk/metagenomics/api and examine the variuos experiment type identifiers.


|info|\  Details about a single project can be retrieved by providing a unique identifier assigned during the archiving process. For example, https://www.ebi.ac.uk/metagenomics/api/latest/studies/ERP009703 provides access to the Ocean Sampling Day (OSD) 2014 project.


|action|\  Retrieve the list of samples contained in this study using the following URL: https://www.ebi.ac.uk/metagenomics/api/latest/studies/ERP009703/samples. Explore the response, at the bottom of the page you can find the number of pages that match this query.


|action|\  Now, retrieve all the analyses performed on this study using: https://www.ebi.ac.uk/metagenomics/api/latest/studies/ERP009703/analyses.


|question|\  Question 2: Is the number of samples the same as the number of analyses?. What could be the reason?


|info|\  Parameters can be added to the URL to filter and sort the data, allowing the construction of more complex queries. The API browser lists the filters that are avaiable, as ilustrated in Figures 2 and 3.

|filters|\
**Figure 2**: Filters menu in MGnify API browser.

|filters_popup|\
**Figure 3**: Filters pop up menu for the Genomes list endpoint.


|question|\  Question 3: Using the API browser, how many results have been analysed with the pipeline version 4.0 for the OSD study ERP009703?





.. |info| image:: media/info.png
   :width: 0.26667in
   :height: 0.26667in
.. |action| image:: media/action.png
   :width: 0.26667in
   :height: 0.26667in
.. |question| image:: media/question.png
   :width: 0.26667in
   :height: 0.26667in

.. |api_overview| image:: media/api/api_overview.png
   :width: 800px
   :target: https://www.ebi.ac.uk/metagenomics/api
   :alt: MGnify API website

.. |filters| image:: media/api/filters_menu.png
   :width: 800px
   :target: https://www.ebi.ac.uk/metagenomics/api
   :alt: MGnify API website

.. |filters_popup| image:: media/api/filters_menu_popup.png
   :width: 800px
   :target: https://www.ebi.ac.uk/metagenomics/api
   :alt: MGnify API website
