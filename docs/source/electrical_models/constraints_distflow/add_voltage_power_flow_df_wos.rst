add_voltage_power_flow_df_wos_constraint
=======================================



Function
--------

.. autofunction:: flexgridpy.electrical_models.constraints.pf.distflow_wo_shunt_constr.add_voltage_power_flow_df_wos_constraint

Manager Method
--------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.add_voltage_power_flow_df_wos_constraint

Description
-----------

Adds the **voltage drop equation** along each branch :math:`(i,j)`.

Mathematical Formulation
------------------------

.. math::

   v_{j,t} = v_{i,t} - 2\left(r_{ij}\,P_{ij,t} + x_{ij}\,Q_{ij,t}\right)
             + \left(r_{ij}^2 + x_{ij}^2\right)\ell_{ij,t}

where:

* :math:`v_{i,t} = |V_{i,t}|^2` — squared voltage magnitude
* :math:`P_{ij,t}, Q_{ij,t}` — branch power flows
* :math:`\ell_{ij,t} = |I_{ij,t}|^2` — squared current

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Argument
     - Description
   * - ``pline_var``, ``qline_var``
     - Active and reactive branch power variables
   * - ``current_var``
     - Squared current variable :math:`\ell_{ij,t}`
   * - ``voltage_var``
     - Squared voltage variable :math:`v_{i,t}`
   * - ``resistance_para``, ``reactance_param``
     - Line :math:`r_{ij}`, :math:`x_{ij}` parameters
   * - ``set``
     - Branch set (typically ``Slines``)
   * - ``name_prefix`` (str)
     - Constraint group name



Example
-------

.. code-block:: python

   mgr.add_voltage_power_flow_df_wos_constraint(
       pline_var=mgr.model.pLine,
       qline_var=mgr.model.qLine,
       current_var=mgr.model.line_curr,
       voltage_var=mgr.model.voltage,
       resistance_para=mgr.model.resistance_Parm,
       reactance_param=mgr.model.reactance_Parm,
       set=mgr.model.Slines,
       name_prefix="VoltageDrop",
   )
