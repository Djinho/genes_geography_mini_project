PCA Analysis on Genetic Data
This project performs Principal Component Analysis (PCA) on genetic data from the 1000 Genomes Project to visualize population structure. It includes a Bash script for downloading the necessary data, a Python script for processing the VCF file into a genotype matrix, and another Python script for PCA and visualization.

Project Overview
Data Download:

The Bash script (get_data.sh) downloads the following files from the 1000 Genomes Project:

A VCF file containing genotypes for chromosome 22 (ALL.chr22.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz).

The corresponding index file (ALL.chr22.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz.tbi).

A population panel file (phase1_integrated_calls.20101123.ALL.panel).

Data Processing:

The Python script (vcf_2_matrix.py) processes the VCF file to extract genotype data and creates a genotype matrix.

It maps sample IDs to population codes and saves the results in a CSV file (matrix.csv).

PCA and Visualization:

The Python script (PCA_visualisations.py) performs PCA on the genotype matrix and generates a scatter plot of the first two principal components, colored by population code.

Requirements
Software:

wget (for downloading files).

Python 3.x with the following libraries:

pysam

numpy

pandas

scikit-learn

altair

Install Dependencies:

bash
Copy
pip install pysam numpy pandas scikit-learn altair
Instructions
Download Data:

Run the Bash script to download the required files:

bash
Copy
bash get_data.sh
Process VCF File:

Run the Python script to convert the VCF file into a genotype matrix:

bash
Copy
python vcf_2_matrix.py
This will generate a CSV file (matrix.csv) containing the genotype matrix and population codes.

Perform PCA and Visualize Results:

Run the Python script to perform PCA and generate the scatter plot:

bash
Copy
python PCA_visualisations.py
The script will display a scatter plot of the first two principal components, colored by population code.

Code Structure
Bash Script (get_data.sh)
Downloads the VCF file, its index, and the population panel file from the 1000 Genomes Project.

Python Script (vcf_2_matrix.py)
Data Extraction:

Reads the VCF file and extracts genotype data.

Maps sample IDs to population codes using the panel file.

Output:

Saves the genotype matrix and population codes in a CSV file (matrix.csv).

Python Script (PCA_visualisations.py)
PCA:

Loads the genotype matrix from matrix.csv.

Performs PCA to reduce dimensionality to 2 components.

Visualization:

Uses Altair to create a scatter plot of the first two principal components, colored by population code.

Example Output
CSV File (matrix.csv):

Contains the genotype matrix with variant IDs as columns, sample IDs as rows, and a column for population codes.

PCA Scatter Plot:

A 2D scatter plot showing the distribution of samples based on the first two principal components, colored by population code.

Notes
The script vcf_2_matrix.py processes every 100th variant to reduce computational load. You can modify this by adjusting the condition if counter % 100 == 0 in the script.

Ensure the input files (VCF and panel) are correctly downloaded and placed in the working directory before running the Python scripts.

License
This project is open-source and available under the MIT License.
