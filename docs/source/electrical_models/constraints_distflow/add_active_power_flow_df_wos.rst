add_active_power_flow_df_wos_constraint
======================================

Description
-----------

Adds the **active power balance** at each bus :math:`j` and time :math:`t` for
the DistFlow formulation. Accounts for DER injection, grid supply, loads, EV
charging, heat-pump consumption, and optional market offers.

Mathematical Formulation
------------------------

.. math::

   \sum_{g} P_{j,t}^g + P_{j,t}^\text{grid} - P_{j,t}^\text{load} - P_{j,t}^\text{EV} - P_{j,t}^\text{HP}
   = \sum_{k \in \mathcal{D}_j} P_{jk,t}
   - \sum_{i \in \mathcal{U}_j} \left( P_{ij,t} - r_{ij}\,\ell_{ij,t} \right)
   + \text{(transformer terms)}

where:

* :math:`\mathcal{D}_j` — downstream buses from :math:`j` (``Sdownstream[j]``)
* :math:`\mathcal{U}_j` — upstream buses to :math:`j` (``Supstream[j]``)
* :math:`r_{ij}` — line resistance (p.u.)
* :math:`\ell_{ij,t}` — squared branch current variable

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Argument
     - Description
   * - ``pder_contrl_var``
     - Controllable DER active power variable
   * - ``pline_var``
     - Line active power flow variable
   * - ``p_transformer_var``
     - Transformer active power flow variable
   * - ``pgrid_var``
     - Grid injection variable at slack bus
   * - ``line_current_var``
     - Squared line current :math:`\ell_{ij,t}`
   * - ``transformer_current_var``
     - Squared transformer current
   * - ``name_prefix`` (str)
     - Constraint group name for registration
   * - ``ev_ch_p_var`` (optional)
     - EV charging active power
   * - ``p_hp_var`` (optional)
     - Heat pump active power
   * - ``p_offer_var`` (optional)
     - Market generator offer dispatch

API Reference
-------------

.. autofunction:: flexgridpy.electrical_models.constraints.pf.distflow_wo_shunt_constr.add_active_power_flow_df_wos_constraint

Manager Wrapper
---------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.add_active_power_flow_df_wos_constraint

Example
-------

.. code-block:: python

   mgr.add_active_power_flow_df_wos_constraint(
       pder_contrl_var=mgr.model.pDER,
       pline_var=mgr.model.pLine,
       p_transformer_var=mgr.model.pTrafo,
       pgrid_var=mgr.model.pGrid,
       line_current_var=mgr.model.line_curr,
       transformer_current_var=mgr.model.trafo_curr,
       name_prefix="ActivePowerBalance",
   )
