## Installation ##
In order to run the notebooks in this repository, the following libraries have to be installed:
1) Pandas 0.24.2
2) Numpy 1.17.4
3) seaborn 0.9.0
4) scikit-learn 0.21.2
5) tensorflow 2.6.0
6) Flask 2.1.3
7) Plotly 5.11

## Project Motivation ##
The purpose of this project is to cluster the input data. The input data consists of data pertaining to a particular commodity. Various clustering methods have been compared and suitable clustering approach has been selected based on the comparison results. 

## Technical Details ##
This project demonstrates:
1) Extensive exploratory data analysis
2) Use of tensorflow.keras to build an auteencoder
3) Use of evaluation metrics to compare clustering approaches
4) Use of CRISP-DM steps

## File Descriptions ##
The repository consists of 2 main folders -- Data & Code </br>
The Data folder has:
1) cmd_attributes_v3_upload.csv: This file has the pre-processed input data

The Code folder has:
1) CMD_Clustering_Steps1_2.ipynb: This is a jupyter notebook showing the first 2 steps of CRISP-DM (Business & data understanding)
2) CMD_Clustering_Steps3_5.ipynb: This is a jupyter notebook showing steps 3, 4 and 5 of CRISP-DM (Data preparation, modeling & evaluation)
3) cmd_data_output.csv: csv file with cluster information and is used in the python script
4) CMD_Clustering_Deploy_Step6.py: This is a python script for a web-app showing details about the clusters
5) index.html & chart_4.html: HTML templates used in the webapp
6) Clustering_Project_v4.pdf: Document describing the overall approach for clustering

Steps for running the python script:
1) cd SKU_Clusters ## go to the location of the repository </br>
2) python ./Code/CMD_Clustering_Deploy_Step6.py

## Acknowledgements ##
Thanks to Python open source community for creating valuable libraries used in this project. <br>
