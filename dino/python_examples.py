"""Small Python and PyYAML syntax examples for the interview exercise.

This file demonstrates mechanics that may be useful during the interview. It
does not implement the dinosaur analysis problem.
"""

from pathlib import Path
from typing import Any

import yaml


def read_yaml_file(path: str | Path) -> dict[str, Any]:
    """Read a YAML file and return its top-level mapping."""
    with open(path, encoding="utf-8") as stream:
        data = yaml.safe_load(stream)

    if not isinstance(data, dict):
        raise ValueError("Expected the YAML document to contain a dictionary")

    return data


def dictionary_examples(record: dict[str, Any]) -> None:
    """Demonstrate direct indexing and the dictionary.get() method."""
    # Direct indexing raises KeyError if the key does not exist.
    name = record["name"]

    # get() returns None when a key does not exist.
    weight = record.get("weight")

    # A second argument supplies a default value.
    habitat = record.get("habitat", "Unknown")

    print(f"{name}: weight={weight}, habitat={habitat}")


if __name__ == "__main__":
    try:
        dataset = read_yaml_file(Path(__file__).with_name("dino.yaml"))
        dinosaurs = dataset.get("dinosaurs", [])

        if dinosaurs:
            dictionary_examples(dinosaurs[0])
        else:
            print("The dataset contains no dinosaurs")
    except FileNotFoundError as error:
        print(f"File not found: {error.filename}")
    except yaml.YAMLError as error:
        print(f"Invalid YAML: {error}")
    except (ValueError, KeyError) as error:
        print(f"Unable to process the dataset: {error}")
