enviroment_profile_param
========================



Function
--------

.. autofunction:: flexgridpy.electrical_models.parameters.enviroment_param.enviroment_profile_param

.. autofunction:: flexgridpy.electrical_models.parameters.enviroment_param.enviroment_profile_stochastic_param

Manager Method
--------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.enviroment_profile_param

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
