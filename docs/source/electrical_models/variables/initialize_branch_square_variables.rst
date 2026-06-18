initialize_branch_square_variables
=================================



Function
--------

.. autofunction:: flexgridpy.electrical_models.variables.def_line_var.initialize_branch_square_variables

.. autofunction:: flexgridpy.electrical_models.variables.def_line_var.initialize_branch_stochastic_variables

Manager Method
--------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.initialize_branch_square_variables

Description
-----------

Creates squared branch current variables :math:`\ell_{ij,t} = |I_{ij,t}|^2` and
branch active/reactive power flow variables for the DistFlow formulation.

Variables Created
-----------------

* Squared current :math:`\ell_{ij,t}` — non-negative, for each line and time
* Active power flow :math:`P_{ij,t}`
* Reactive power flow :math:`Q_{ij,t}`




See Also
--------

* :doc:`../constraints_distflow/add_brunch_current_flow_df_wos_SOCP`
