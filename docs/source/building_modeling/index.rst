Building Modeling
=================

FlexGridPy provides grey-box RC (Resistance-Capacitance) models for building
thermal dynamics and heat-pump operation. The building modeling module supports
**parameter tuning** (fitting R/C values from measured data), **simulation**, and
integration with the electrical optimization model.

.. toctree::
   :maxdepth: 2
   :caption: Building Modeling

   overview
   temperature_tuning
   heating_power_tuning
   simulation
   heat_pump
   weather_data
   dataset_tools

Quick Links
-----------

* :doc:`temperature_tuning` — Fit indoor temperature RC models
* :doc:`heating_power_tuning` — Fit heating power models
* :doc:`simulation` — Forward simulation after tuning
* :doc:`heat_pump` — COP regression model
