DistFlow Constraints
====================

The DistFlow (without shunt) formulation is a convex OPF model for radial
distribution networks. It uses squared voltage variables :math:`v_i = |V_i|^2` and
squared branch current variables :math:`\ell_{ij} = |I_{ij}|^2`.

Recommended build order:

1. ``initialize_voltage_square_variables``
2. ``initialize_branch_square_variables``
3. Active power balance → Reactive power balance → Voltage drop → Branch current

.. toctree::
   :maxdepth: 1

   constraints_distflow/add_active_power_flow_df_wos
   constraints_distflow/add_reactive_power_flow_df_wos
   constraints_distflow/add_voltage_power_flow_df_wos
   constraints_distflow/add_brunch_current_flow_df_wos_equal
   constraints_distflow/add_brunch_current_flow_df_wos_SOCP
   constraints_distflow/check_socp_exactness

Reference
---------

Based on the branch flow model for radial networks (DistFlow equations without
shunt admittance).
