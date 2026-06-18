Electrical Models
=================

FlexGridPy builds a **Pyomo optimization problem** on top of a
`pandapower <https://pandapower.readthedocs.io>`_ network via the
:class:`~flexgridpy.electrical_models.Manager.Manager` class.

Each function has its own page in the sidebar, with signature, parameters, equations, and examples.

.. rubric:: Recommended Workflow


.. code-block:: python

   mgr = Manager(net)
   mgr.addTime(timeframe=24, time_interval=60)
   mgr.initialize_sets()
   mgr.line_param(Y_bus, ...)
   mgr.load_profile_param(profiles, "Load_P", "Load_Q")
   mgr.initialize_voltage_square_variables("voltage")
   mgr.add_active_power_flow_df_wos_constraint(...)
   mgr.add_brunch_current_flow_df_wos_SOCP_constraint(...)

.. toctree::
   :maxdepth: 2

   manager
   sets
   parameters
   variables
   constraints_distflow
   constraints_bfm
   constraints_ac_pf
   constraints_flow
   constraints_ev
   constraints_hp_dhw
   constraints_stochastic
   power_flow
   initializations
