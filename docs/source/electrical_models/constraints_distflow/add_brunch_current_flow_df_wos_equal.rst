add_brunch_current_flow_df_wos_equal
=====================================

Description
-----------

Adds the **exact** branch current relation (non-convex equality).

Mathematical Formulation
------------------------

.. math::

   \ell_{ij,t} \cdot v_{i,t} = P_{ij,t}^2 + Q_{ij,t}^2

This is the equality form of the power-current relation. For a convex
relaxation, use the SOCP version instead
(:doc:`add_brunch_current_flow_df_wos_SOCP`).

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Argument
     - Description
   * - ``pline_var``, ``qline_var``
     - Branch active/reactive power variables
   * - ``current_var``
     - Squared current :math:`\ell_{ij,t}`
   * - ``volage_var``
     - Squared voltage :math:`v_{i,t}`
   * - ``set``
     - Branch set
   * - ``name_prefix`` (str)
     - Constraint group name

API Reference
-------------

.. autofunction:: flexgridpy.electrical_models.constraints.pf.distflow_wo_shunt_constr.add_brunch_current_flow_df_wos_equal_constraint

Manager Wrapper
---------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.add_brunch_current_flow_df_wos_equal_constraint

When to Use
-----------

Use the exact form only when the problem remains tractable (e.g. with binary
variables for exactness recovery). For large networks, prefer the SOCP relaxation.
