add_reactive_power_flow_df_wos_constraint
========================================

Function
--------

.. code-block:: python

   add_reactive_power_flow_df_wos_constraint(manager, qder_contr_var, qline_var, q_transformer_var, qgrid_var, line_current_var, transformer_current_var, name_prefix, ev_ch_q_var=None, q_hp_var=None)

**Module:** ``flexgridpy.electrical_models.constraints.pf.distflow_wo_shunt_constr``

Manager Method
--------------

.. code-block:: python

   mgr.add_reactive_power_flow_df_wos_constraint(...)

Description
-----------

Adds the **reactive power balance** at each bus :math:`j` and time :math:`t`.

Mathematical Formulation
------------------------

.. math::

   \sum_{g} Q_{j,t}^g + Q_{j,t}^\text{grid} - Q_{j,t}^\text{load} - Q_{j,t}^\text{EV} - Q_{j,t}^\text{HP}
   = \sum_{k \in \mathcal{D}_j} Q_{jk,t}
   - \sum_{i \in \mathcal{U}_j} \left( Q_{ij,t} - x_{ij}\,\ell_{ij,t} \right)
   + \text{(transformer terms)}

where :math:`x_{ij}` is the line reactance (p.u.).

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Argument
     - Description
   * - ``qder_contr_var``
     - Controllable DER reactive power variable
   * - ``qline_var``
     - Line reactive power flow variable
   * - ``q_transformer_var``
     - Transformer reactive power flow variable
   * - ``qgrid_var``
     - Grid reactive injection variable
   * - ``line_current_var``
     - Squared line current :math:`\ell_{ij,t}`
   * - ``transformer_current_var``
     - Squared transformer current
   * - ``name_prefix`` (str)
     - Constraint group name
   * - ``ev_ch_q_var`` (optional)
     - EV reactive charging power
   * - ``q_hp_var`` (optional)
     - Heat pump reactive power
