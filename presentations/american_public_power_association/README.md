# American Public Power Association — OpenDSS storage examples

This folder contains self-contained **Jupyter** notebooks for **OpenDSS** and **Python** that illustrate how **energy storage** on a distribution feeder interacts with **active power at the feederhead** in two common storylines: **peak shaving** and **PV causing reverse power flow at the feederhead**.

## Purpose

The main goals of this set are:

- to show a **base case** (feeder with loads only) and how **P at the feederhead** and a **24-hour** load pattern are read in OpenDSS
- to show **peak shaving**: storage **discharging** in high-import hours to **reduce stress** on the upstream path (substation, transmission) and the need to **recharge** in other hours
- to show **storage with PV**: when **export/reverse power flow** at the feederhead is not allowed, storage may **charge** in high-PV hours
- to use `set number=72` to run **72 one-hour** steps (three 24 h days of the same daily shapes) so **charge, discharge, and state of charge** are easier to interpret

## Getting started

These notebooks are easy to run in **Google Colab** (see the first code cells) or **locally** with the same dependencies.

## Notebooks (order suggested)

- `base_case.ipynb` — **Loads only**: snapshot and daily results; reference **P at the feeder feederhead**.
- `peakshaving_example.ipynb` — Adds **Storage** and **StorageController** for **peak shaving**; multi-day `number=72` run.
- `storage_pv_example.ipynb` — Adds a **Generator**-style **PV** profile, then **Storage** to manage **feederhead export** and **optional** peak support.

Feeder used in the examples: **EPRITestCircuits ckt5** under `feeder_models/EPRITestCircuits/ckt5/`.

## Repository and resources

These examples are part of **[PauloRadatz/opendss-python-examples](https://github.com/PauloRadatz/opendss-python-examples)**.

More learning materials: [pauloradatz.me](https://www.pauloradatz.me) and [OpenDSS courses](https://www.pauloradatz.me/opendss-courses).

## Contact

- Paulo Radatz
- Email: [paulo.radatz@gmail.com](mailto:paulo.radatz@gmail.com)
- LinkedIn: [linkedin.com/in/pauloradatz](https://www.linkedin.com/in/pauloradatz/)
