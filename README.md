cat > README.md << 'EOF'
# TME Deconvolution Pipeline

A modular bioinformatics workflow for tumor
microenvironment characterization using bulk RNA-seq.

## Main modules

- RNA-seq quality control
- Transcript quantification with Kallisto
- Gene-level TPM estimation
- Immune cell deconvolution:
  - EPIC
  - quanTIseq
  - xCell
  - MCP-counter
- Clinical and molecular data integration
- Statistical analysis
- Visualization
- Flow cytometry validation

## Workflow engine

Snakemake

## Programming languages

R and Python
EOF