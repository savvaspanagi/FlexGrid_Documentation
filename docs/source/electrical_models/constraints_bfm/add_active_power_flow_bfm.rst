add_active_power_flow_bfm
==========================



Function
--------

.. autofunction:: flexgridpy.electrical_models.constraints.pf.BFM_wshunt_radial_constr.add_active_power_flow_bfm

Manager Method
--------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.add_active_power_flow_bfm

Description
-----------

Adds the **active power balance** at each bus for the Branch Flow Model (BFM).
Unlike DistFlow, BFM uses separate forward and reverse line flow variables.

Mathematical Formulation
------------------------

.. math::

   \sum P_{j,t}^\text{gen} - P_{j,t}^\text{load} - P_{j,t}^\text{EV} - P_{j,t}^\text{HP}
   = \sum_{k \in \mathcal{D}_j} P_{jk,t}
   + \sum_{i \in \mathcal{U}_j} P_{ij,t}^\text{rev}
   + \text{(transformer terms)}

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Argument
     - Description
   * - ``pder_contrl_var``
     - Controllable DER active power
   * - ``p_line_var``, ``p_line_reverse_var``
     - Forward and reverse line active power flows
   * - ``p_transformer_var``, ``p_transformer_reverse_var``
     - Forward and reverse transformer flows
   * - ``pgrid_var``
     - Grid injection at slack bus
   * - ``ev_ch_p_var``
     - EV charging power
   * - ``p_hp_var`` (optional)
     - Heat pump electrical power
   * - ``name_prefix`` (str)
     - Constraint group name
