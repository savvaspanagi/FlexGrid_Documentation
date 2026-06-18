add_current_flow_bfm
======================

Function
--------

.. code-block:: python

   add_current_flow_bfm(manager, line_set, line_reverse_set, p_line_var, p_reverse_line_par, q_line_var, q_reverse_line_par, current_var, curret_reverse_line_var, voltage_var, name_prefix, name_reverse_prefix)

**Module:** ``flexgridpy.electrical_models.constraints.pf.BFM_wshunt_radial_constr``

Manager Method
--------------

.. code-block:: python

   mgr.add_current_flow_bfm(...)

Description
-----------

Adds the **branch current relation** for the BFM formulation (exact equality).

Mathematical Formulation
------------------------

.. math::

   \ell_{ij,t} \cdot v_{i,t} = P_{ij,t}^2 + Q_{ij,t}^2

Both forward and reverse line directions are constrained.


See Also
--------

* :doc:`../constraints_distflow/add_brunch_current_flow_df_wos_SOCP` — SOCP relaxation alternative
