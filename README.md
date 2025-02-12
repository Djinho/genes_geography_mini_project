# **PCA Analysis on Genetic Data**

This project performs Principal Component Analysis (PCA) on genetic data from the 1000 Genomes Project to visualize population structure. It includes a Bash script for downloading the necessary data, a Python script for processing the VCF file into a genotype matrix, and another Python script for PCA and visualization.

---

## **Project Overview**

1. **Data Download**:
   - The Bash script (`get_data.sh`) downloads the following files from the 1000 Genomes Project:
     - A VCF file containing genotypes for chromosome 22 (`ALL.chr22.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz`).
     - The corresponding index file (`ALL.chr22.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz.tbi`).
     - A population panel file (`phase1_integrated_calls.20101123.ALL.panel`).

2. **Data Processing**:
   - The Python script (`vcf_2_matrix.py`) processes the VCF file to extract genotype data and creates a genotype matrix.
   - It maps sample IDs to population codes and saves the results in a CSV file (`matrix.csv`).

3. **PCA and Visualization**:
   - The Python script (`PCA_visualisations.py`) performs PCA on the genotype matrix and generates a scatter plot of the first two principal components, colored by population code.

---

## **Requirements**

- **Software**:
  - `wget` (for downloading files).
  - Python 3.x with the following libraries:
    - `pysam`
    - `numpy`
    - `pandas`
    - `scikit-learn`
    - `altair`

- **Install Dependencies**:
  ```bash
  pip install pysam numpy pandas scikit-learn altair
