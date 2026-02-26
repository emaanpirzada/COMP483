library(sleuth)
library(dplyr)

# Gets all the kallisto samples
samples <-dir("Outputs/Kallisto/samples")
samples

# Assigns the conditions
condition <- c("2dpi", "6dpi", "2dpi", "6dpi")

# Creates a metadata table
metadata_table <- data.frame(sample = samples, condition = condition, stringsAsFactors=FALSE)

# Adds a path column to the metadata table
metadata_table <- metadata_table %>%
   mutate(path=file.path("Outputs/Kallisto/samples", sample))

# Creates the sleuth object
sleuth_object <- sleuth_prep(metadata_table, ~ condition)

# Fits the model
sleuth_object <- sleuth_fit(sleuth_object, ~ condition, 'full')
sleuth_object <- sleuth_fit(sleuth_object, ~1, 'reduced')

# Runs a likelihood ratio test
sleuth_object <- sleuth_lrt(sleuth_object, 'reduced', 'full')

# Extracts results
results_table <- sleuth_results(sleuth_object, 'reduced:full', 'lrt')

# Filters only the significant transcrips (FDR < 0.05)
sig_transcrips <- results_table %>%
   filter(qval < 0.05) %>%
   select(target_id, test_stat, pval, qval)

# Writes all significant transcripts to a txt file
write.table(sig_transcrips, file = "Outputs/Kallisto/sleuth.txt", sep = "\t", quote = FALSE, row.names = FALSE)