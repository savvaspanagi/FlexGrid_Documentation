add_brunch_current_flow_df_wos_SOCP
====================================

Description
-----------

Adds the **SOCP relaxation** of the branch current relation. This makes the
OPF problem convex and solvable with conic solvers (e.g. ECOS, MOSEK).

Mathematical Formulation
------------------------

.. math::

   \ell_{ij,t} \cdot v_{i,t} \geq P_{ij,t}^2 + Q_{ij,t}^2

The inequality is tight (exact) when the optimal solution satisfies:

.. math::

   \ell_{ij,t} \cdot v_{i,t} = P_{ij,t}^2 + Q_{ij,t}^2

Use :doc:`check_socp_exactness` after solving to verify tightness.

Arguments
---------

Same as :doc:`add_brunch_current_flow_df_wos_equal`.

API Reference
-------------

.. autofunction:: flexgridpy.electrical_models.constraints.pf.distflow_wo_shunt_constr.add_brunch_current_flow_df_wos_SOCP_constraint

Manager Wrapper
---------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.add_brunch_current_flow_df_wos_SOCP_constraint

Example
-------

.. code-block:: python

   mgr.add_brunch_current_flow_df_wos_SOCP_constraint(
       pline_var=mgr.model.pLine,
       qline_var=mgr.model.qLine,
       current_var=mgr.model.line_curr,
       volage_var=mgr.model.voltage,
       set=mgr.model.Slines,
       name_prefix="CurrentSOCP",
   )

   # After solving:
   violations = mgr.check_socp_exactness(
       mgr.model.pLine, mgr.model.qLine,
       mgr.model.line_curr, mgr.model.voltage,
       mgr.model.Slines, mgr.model.STimes,
   )
