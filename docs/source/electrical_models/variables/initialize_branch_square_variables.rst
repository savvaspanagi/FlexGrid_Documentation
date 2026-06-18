initialize_branch_square_variables
=================================

Function
--------

.. code-block:: python

   initialize_branch_square_variables(manager, line_set, line_curr_name_prefix=None)

**Module:** ``flexgridpy.electrical_models.variables.def_line_var``

.. code-block:: python

   initialize_branch_stochastic_variables(manager, line_set, system_data_df, line_curr_name_prefix=None, line_rea_curr_name_prefix=None, line_act_curr_name_prefix=None, line_losses_name_prefix=None)

**Module:** ``flexgridpy.electrical_models.variables.def_line_var``

Manager Method
--------------

.. code-block:: python

   mgr.initialize_branch_square_variables(...)

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
