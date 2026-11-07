
import csv
from pathlib import Path


def validate_samples(samples_file):
    """Validate the structure and contents of a sample sheet."""

    samples_file = Path(samples_file)

    if not samples_file.exists():
        raise FileNotFoundError(
            f"Sample sheet not found: {samples_file}"
        )

    required_columns = {
        "sample",
        "layout",
        "fastq_1",
        "fastq_2"
    }

    with open(samples_file, newline="") as file:
        reader = csv.DictReader(file, delimiter="\t")

        if not reader.fieldnames:
            raise ValueError("Sample sheet is empty")

        missing_columns = required_columns - set(reader.fieldnames)

        if missing_columns:
            raise ValueError(
                f"Missing columns: {missing_columns}"
            )

        samples = list(reader)

    if not samples:
        raise ValueError("No samples found in sample sheet")

    sample_ids = [row["sample"].strip() for row in samples]

    if any(not sample for sample in sample_ids):
        raise ValueError("Empty sample ID found")

    if len(sample_ids) != len(set(sample_ids)):
        raise ValueError("Duplicate sample IDs found")

    for row in samples:
        sample = row["sample"].strip()
        layout = row["layout"].strip()
        fastq_1 = row["fastq_1"].strip()
        fastq_2 = row["fastq_2"].strip()

        if layout not in {"paired", "single"}:
            raise ValueError(
                f"Invalid layout for {sample}: {layout}"
            )

        if not fastq_1:
            raise ValueError(
                f"Missing fastq_1 for {sample}"
            )

        if layout == "paired" and not fastq_2:
            raise ValueError(
                f"Missing fastq_2 for paired-end sample {sample}"
            )

        if layout == "single" and fastq_2:
            raise ValueError(
                f"Single-end sample {sample} should not have fastq_2"
            )

    print(f"Successfully validated {len(samples)} samples!")

    for row in samples:
        print(f"{row['sample']}: {row['layout']}")

    return samples


if __name__ == "__main__":
    validate_samples("config/samples.tsv")
