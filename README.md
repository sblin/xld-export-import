# Sample scripts to demonstrate how to export/import CIs using XLDeploy cli.

## Installation

Copy the two files script in a working directory

## Requirements

XL Deploy cli is already installed

## Usage:
- Modify the working directory in the export.py and import.py files
- To export data run:

```
cli.sh -f [path_to_workingdir]/export.py
```

- To import data run:

```
cli.sh -f [path_to_workingdir]/import.py
```

- If some apps should be deleted before exporting you can run the script delete_apps.py

```
cli.sh -f [path_to_workingdir]/delete_apps.py
```
