Building Modeling
=================

FlexGridPy provides grey-box RC (Resistance-Capacitance) models for building
thermal dynamics and heat-pump operation. The building modeling module supports
**parameter tuning** (fitting R/C values from measured data), **simulation**, and
integration with the electrical optimization model.

.. toctree::
   :maxdepth: 2
   :caption: Building Modeling

   building_modeling/overview
   building_modeling/temperature_tuning
   building_modeling/heating_power_tuning
   building_modeling/simulation
   building_modeling/heat_pump
   building_modeling/weather_data
   building_modeling/dataset_tools

Quick Links
-----------

* :doc:`building_modeling/temperature_tuning` — Fit indoor temperature RC models
* :doc:`building_modeling/heating_power_tuning` — Fit heating power models
* :doc:`building_modeling/simulation` — Forward simulation after tuning
* :doc:`building_modeling/heat_pump` — COP regression model
