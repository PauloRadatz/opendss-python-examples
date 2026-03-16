# ENGR 330 - Power System Seminar Series
## Spring 2026 - Charleston Southern University

This folder contains OpenDSS and Python examples prepared for the **Spring 2026 ENGR 330 Power System Seminar Series** offered through the **Department of Engineering at Charleston Southern University, South Carolina**.

Special thanks to **[Professor Joshua Y. Kim](https://www.linkedin.com/in/070115yikim/)** for the invitation and for the opportunity to share these materials with the students.

## Purpose

These materials were prepared to support the **ENGR 330 Power Systems** course by connecting classroom concepts to a practical engineering workflow for **Solar PV Hosting Capacity analysis** using **OpenDSS** and **Python**.

The main goals of this seminar set are:

- to provide a clear, hands-on introduction to a typical Hosting Capacity workflow, including feeder setup, PV placement and sizing, simulation, and result interpretation
- to help students use OpenDSS and Python together to evaluate distribution-system constraints such as voltage limits and thermal loading
- to offer practical examples that can serve as a starting point for deeper Hosting Capacity studies

## Getting started

These notebooks are intended to be practical, educational, and easy to run in **Google Colab**.

To begin:

- open the notebook for the seminar topic you want to explore
- make sure the repository structure is preserved so feeder files can be loaded correctly (clone the repo or run from within it)
- review the inputs in each notebook, such as feeder choice, bus selection, operating condition, and stopping criterion

## Repository structure

These examples are part of the repository **[PauloRadatz/opendss-python-examples](https://github.com/PauloRadatz/opendss-python-examples)**.

Each notebook is self-contained and does not depend on external Python scripts. Available notebooks:

- `overvoltage.ipynb` — Overvoltage hosting capacity (single bus)
- `overvoltage_centralized.ipynb` — Centralized overvoltage hosting capacity (all buses, plotted on circuit)
- `overvoltage_distributed_fixed_locations.ipynb` — Distributed overvoltage hosting capacity (fixed bus locations, compares two scenarios)
- `overvoltage_distributed_fixed_locations_monte_carlo.ipynb` — Distributed overvoltage hosting capacity with Monte Carlo random bus selection
- `thermal_gen.ipynb` — Thermal (line/transformer loading) hosting capacity

Feeder models used in the notebooks are stored under:

- `feeder_models/`

## Background reference

Some of the ideas illustrated in these examples are related to concepts presented in this public EPRI webinar:

- [EPRI event page](https://www.epri.com/events/1828f14b-73a7-4901-a753-f914a26c4c5a)

## Notes

- These notebooks are meant for educational use.
- The examples are intentionally structured to keep the workflow clear and easy to follow.
- You can adapt the feeder, bus, operating condition, or stopping criterion to explore additional scenarios.

## Additional learning resources

If you would like to continue learning OpenDSS and Python for power-system studies, you can find more materials here:

- [pauloradatz.me](https://www.pauloradatz.me)
- [OpenDSS courses](https://www.pauloradatz.me/opendss-courses)

## Contact

For questions or follow-up about these materials:

- Paulo Radatz
- Email: [paulo.radatz@gmail.com](mailto:paulo.radatz@gmail.com)
- LinkedIn: [linkedin.com/in/pauloradatz](https://www.linkedin.com/in/pauloradatz/)
- Website: [pauloradatz.me](https://www.pauloradatz.me/)
