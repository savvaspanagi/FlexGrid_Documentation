line_param
==========

Description
-----------

Registers per-unit line resistance :math:`R_{ij}`, reactance :math:`X_{ij}`, and
the full bus admittance matrix :math:`\mathbf{Y}_\text{bus}` as Pyomo parameters.
Values are extracted from ``anc_Vars.System_Data_Lines`` and the pre-computed
Y-bus matrix.

Parameters Registered
---------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Prefix argument
     - Pyomo Param
   * - ``resist_prefix``
     - :math:`R_{ij}` for each line :math:`(i,j) \in \mathcal{L}`
   * - ``react_prefix``
     - :math:`X_{ij}` for each line :math:`(i,j) \in \mathcal{L}`
   * - ``adm_real_prefix``
     - :math:`\Re\{Y_{ik}\}` — real part of Y-bus
   * - ``adm_img_prefix``
     - :math:`\Im\{Y_{ik}\}` — imaginary part of Y-bus

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``Y_bus_df`` (DataFrame)
     - Complex admittance matrix indexed by bus pairs
   * - ``resist_prefix`` (str)
     - Name for resistance parameter (e.g. ``"resistance_Parm"``)
   * - ``react_prefix`` (str)
     - Name for reactance parameter
   * - ``adm_real_prefix`` (str)
     - Name for real admittance matrix
   * - ``adm_img_prefix`` (str)
     - Name for imaginary admittance matrix

Per-Unit System
---------------

Line impedances are stored in per-unit on the system base
``anc_Vars.S_Base`` (MVA) and nominal voltage.

API Reference
-------------

.. autofunction:: flexgridpy.electrical_models.parameters.line_param_fun.line_param

Manager Wrapper
---------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.line_param

Example
-------

.. code-block:: python

   from flexgridpy.electrical_models.admittance_matrix.makeYbus import makeYbus

   Y_bus = makeYbus(mgr.net, mgr.anc_Vars)
   mgr.line_param(
       Y_bus,
       resist_prefix="resistance_Parm",
       react_prefix="reactance_Parm",
       adm_real_prefix="admitt_mat_Parm_real",
       adm_img_prefix="admitt_mat_Parm_imag",
   )
