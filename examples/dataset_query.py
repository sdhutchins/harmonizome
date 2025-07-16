from harmonizome import Harmonizome

gene = "STAT3"
gene_data = Harmonizome.get_gene_data(gene, use_cache=True)

# Get all associations as a DataFrame
df = gene_data.to_dataframe()

# Example: select a dataset by name (replace with your choice)
selected_dataset = df["dataset"].unique()[0]  # or set to any dataset name from the list
print(f"\nSelected dataset: {selected_dataset}")

# Filter associations for the selected dataset
dataset_df = df[df["dataset"] == selected_dataset]
print(dataset_df)

# Save to CSV
safe_name = selected_dataset.replace(" ", "_").replace("/", "_")
dataset_df.to_csv(f"{gene.lower()}_{safe_name}_associations.csv", index=False)
print(f"Saved {len(dataset_df)} associations for dataset '{selected_dataset}' to {gene.lower()}_{safe_name}_associations.csv")