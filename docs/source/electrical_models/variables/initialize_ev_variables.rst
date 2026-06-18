initialize_ev_variables
=======================

Function
--------

.. code-block:: python

   initialize_ev_variables(manager, pch_name_prefix, q_name_prefix, soc_name_prefix)

**Module:** ``flexgridpy.electrical_models.variables.def_ev_var``

.. code-block:: python

   initialize_ev_variables_stochastic(manager, pch_name_prefix, q_name_prefix, soc_name_prefix, q_name_prefix_scenario=None, individually_dp=True)

**Module:** ``flexgridpy.electrical_models.variables.def_ev_var``

Manager Method
--------------

.. code-block:: python

   mgr.initialize_ev_variables(...)

Description
-----------

Creates EV charging power and state-of-charge variables for each EV bus and
time step.

Variables Created
-----------------

* ``pEVch[i, t]`` — charging active power (p.u.)
* ``EVsoc[i, t]`` — battery energy / state of charge (p.u.·h)

Bounds
------

Charging power is bounded by ``ev_min_ch_param`` and ``ev_max_ch_param``.
SoC is bounded by ``EV_SoC_min_pref_param`` and ``EV_SoC_max_param``.


See Also
--------

* :doc:`../constraints_ev/add_ev_soc_constraint`
* :doc:`../parameters/initialize_ev_params`
