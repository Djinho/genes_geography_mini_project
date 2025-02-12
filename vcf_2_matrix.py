from pysam import VariantFile  # For reading VCF files
import numpy as np  # For numerical operations
from sklearn import decomposition  # For PCA
import pandas as pd  # For data manipulation and CSV export

# File paths for the VCF and panel files
vcf_filename = "ALL.chr22.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz"
panel_filename = "phase1_integrated_calls.20101123.ALL.panel"

# Initialize lists to store genotypes, sample IDs, and variant IDs
genotypes = []
samples = []
variant_ids = []

# Open the VCF file and read records
with VariantFile(vcf_filename) as vcf_reader:
    counter = 0
    for record in vcf_reader:
        counter += 1
        # Process every 100th record to reduce data size
        if counter % 100 == 0:
            # Extract allele indices for each sample
            alleles = [record.samples[x].allele_indices for x in record.samples]
            samples = [sample for sample in record.samples]
            genotypes.append(alleles)
            variant_ids.append(record.id)
        # Print progress every 4943 records
        if counter % 4943 == 0:
            print(counter)
            print(f'{round(100 * counter / 494328)}%')
        # Uncomment to limit the number of records processed (for testing)
        # if counter >= 10000:
        #     break

# Read the panel file to map sample IDs to population codes
with open(panel_filename) as panel_file:
    labels = {}  # Dictionary to store {sample_id: population_code}
    for line in panel_file:
        line = line.strip().split('\t')
        labels[line[0]] = line[1]

# Print variant IDs and check the shape of the genotypes array
print(variant_ids)
genotypes = np.array(genotypes)
print(genotypes.shape)

# Count non-zero alleles to create a genotype matrix
matrix = np.count_nonzero(genotypes, axis=2)

# Transpose the matrix for PCA (samples as rows, variants as columns)
matrix = matrix.T
print(matrix.shape)

# Perform PCA with 2 components
pca = decomposition.PCA(n_components=2)
pca.fit(matrix)
print(pca.singular_values_)  # Print singular values from PCA
to_plot = pca.transform(matrix)  # Transform data into 2D PCA space
print(to_plot.shape)

# Create a DataFrame with the matrix, variant IDs, and population codes
df = pd.DataFrame(matrix, columns=variant_ids, index=samples)
df['Population code'] = df.index.map(labels)
df.to_csv("matrix.csv")  # Save the DataFrame to a CSV file
