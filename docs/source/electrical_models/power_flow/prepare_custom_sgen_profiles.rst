prepare_custom_sgen_profiles
============================

Function
--------

.. code-block:: python

   prepare_custom_sgen_profiles(manager, p_controll_mw, q_controll_mvar, p_uncontroll_mw, q_uncontroll_mvar)

**Module:** ``flexgridpy.electrical_models.power_flow.sgen_input``

Manager Method
--------------

.. code-block:: python

   mgr.prepare_custom_sgen_profiles(...)

Prepares custom generator profiles from OPF results.

Example
-------

.. code-block:: python

   mgr.prepare_custom_sgen_profiles()
