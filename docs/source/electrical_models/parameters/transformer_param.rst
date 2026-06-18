transformer_param
=================

Description
-----------

Registers per-unit transformer resistance and reactance as Pyomo parameters,
extracted from ``anc_Vars.System_Data_Transformers``.

Also see :meth:`~flexgridpy.electrical_models.Manager.Manager.transformer_nominal_power_param`
for the nominal power rating :math:`S_n`.

Parameters Registered
---------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Prefix
     - Content
   * - ``resist_prefix``
     - :math:`R_{ij}^T` — transformer resistance (p.u.)
   * - ``react_prefix``
     - :math:`X_{ij}^T` — transformer reactance (p.u.)

API Reference
-------------

.. autofunction:: flexgridpy.electrical_models.parameters.transformer_param_fun.transformer_param

.. autofunction:: flexgridpy.electrical_models.parameters.transformer_param_fun.transformer_nominal_power_param

Manager Wrapper
---------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.transformer_param

.. automethod:: flexgridpy.electrical_models.Manager.Manager.transformer_nominal_power_param
