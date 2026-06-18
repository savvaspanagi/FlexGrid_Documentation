add_current_flow_bfm
======================



Function
--------

.. autofunction:: flexgridpy.electrical_models.constraints.pf.BFM_wshunt_radial_constr.add_current_flow_bfm

Manager Method
--------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.add_current_flow_bfm

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
