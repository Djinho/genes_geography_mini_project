#!/bin/bash

# This script downloads files from 42basepairs using wget.
# Ensure wget is installed before running this script.

# Set the base URL for easier maintenance
BASE_URL="https://42basepairs.com/download/s3/1000genomes/release/20110521"

# Function to check if wget is installed
if ! command -v wget &> /dev/null; then
    echo "Error: wget is not installed. Please install wget and rerun the script."
    exit 1
fi

# Download VCF file containing SNPs, indels, and structural variants genotypes
wget -q --show-progress "${BASE_URL}/ALL.chr22.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz"

# Download the corresponding index file (TBI) for the VCF file
wget -q --show-progress "${BASE_URL}/ALL.chr22.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz.tbi"

# Download the population panel file
wget -q --show-progress "${BASE_URL}/phase1_integrated_calls.20101123.ALL.panel"

# Print a message when downloads are complete
echo "Download complete."
