# IEEE ET / PES / PELS Joint Chapter Workshop
## OpenDSS for Distribution System Analysis: From Fundamentals to Python Automation

This folder contains the Jupyter notebooks for the **IEEE ET / PES / PELS Joint Chapter Workshop**.

## Purpose

These materials support the workshop and are designed to take participants from a foundational understanding of OpenDSS as a standalone simulator into Python-based automation with `py-dss-interface` and `py-dss-toolkit`.

The main goals of this set are:

- to show how a typical OpenDSS run file translates directly into Python through `dss.text(...)`
- to demonstrate why Python automation matters in practice — sweeping conditions, screening results, building reproducible workflows
- to introduce `py-dss-toolkit` and the cleaner, more visual workflows it enables
- to give participants a clear picture of OpenDSS as a programmable engineering platform when paired with Python

## Getting started

Each notebook is intended to run cleanly in **Google Colab** from top to bottom. The first code cell installs the dependencies and clones the repository so the `ckt5` feeder is available.

To begin:

- open the notebook for the topic you want to explore
- run the cells in order
- adapt the load level, the feeder, or the analysis to explore additional scenarios

## Notebooks (suggested order)

- `01_opendss_workflow_with_py_dss_interface.ipynb` — Translate a typical OpenDSS run file into Python using only `py-dss-interface`. Compile, send commands, set parameters, solve, read results.
- `02_load_level_sweep.ipynb` — Sweep the load multiplier across the feeder, capture key metrics in a DataFrame, and visualize them. The "why automate?" notebook.
- `03_finding_lowest_voltage_bus.ipynb` — Find the worst-voltage node on the feeder in two lines, then expand the question with pandas.
- `04_introduction_to_py_dss_toolkit.ipynb` — Re-do the same workflow with `py-dss-toolkit`. Structured DataFrames, ready-made result tables, voltage profile, and circuit map in one line each.

Feeder used in the examples: **EPRITestCircuits ckt5** under `feeder_models/EPRITestCircuits/ckt5/`.

## Workshop message

OpenDSS works fine on its own. With `py-dss-interface`, every OpenDSS command becomes scriptable from Python. With `py-dss-toolkit`, the common engineering workflows become short and visual. Together they turn OpenDSS into a programmable engineering platform.

## Repository and resources

These examples are part of **[PauloRadatz/opendss-python-examples](https://github.com/PauloRadatz/opendss-python-examples)**.

More learning materials: [pauloradatz.me](https://www.pauloradatz.me) and [OpenDSS courses](https://www.pauloradatz.me/opendss-courses).

## Contact

- Paulo Radatz
- Email: [paulo.radatz@gmail.com](mailto:paulo.radatz@gmail.com)
- LinkedIn: [linkedin.com/in/pauloradatz](https://www.linkedin.com/in/pauloradatz/)
- Website: [pauloradatz.me](https://www.pauloradatz.me/)
