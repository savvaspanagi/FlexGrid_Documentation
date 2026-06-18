enviroment_profile_param
========================

Function
--------

.. code-block:: python

   enviroment_profile_param(manager, data, outdoor_temeprature_name_prefix, solar_irradiance_name_prefix)

**Module:** ``flexgridpy.electrical_models.parameters.enviroment_param``

.. code-block:: python

   enviroment_profile_stochastic_param(manager, temp_data, ghi_data, outdoor_temeprature_name_prefix, solar_irradiance_name_prefix)

**Module:** ``flexgridpy.electrical_models.parameters.enviroment_param``

Manager Method
--------------

.. code-block:: python

   mgr.enviroment_profile_param(...)

Description
-----------

Registers time-series outdoor temperature :math:`T_\text{out}` and global
horizontal irradiance :math:`G_\text{HI}` profiles used in building
thermodynamic constraints.

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Argument
     - Description
   * - ``tout_profile`` (Series/DataFrame)
     - Outdoor temperature profile aligned with ``STimes``
   * - ``ghi_profile`` (Series/DataFrame)
     - Solar irradiance profile aligned with ``STimes``
   * - ``tout_prefix``, ``ghi_prefix``
     - Registered parameter names


See Also
--------

* :doc:`../../building_modeling/weather_data`
