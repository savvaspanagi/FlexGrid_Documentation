Power Flow Utilities
====================

Utilities for comparing optimization results against pandapower power flow and
for preparing input profiles from solved OPF results.

Compare PF vs OPF
-----------------

.. autofunction:: flexgridpy.electrical_models.power_flow.compare_pf_vs_opf.compare_results

Generator Profiles
------------------

.. autofunction:: flexgridpy.electrical_models.power_flow.sgen_input.prepare_sgen_profiles

.. autofunction:: flexgridpy.electrical_models.power_flow.sgen_input.prepare_custom_sgen_profiles

Load Profiles
-------------

.. autofunction:: flexgridpy.electrical_models.power_flow.load_input.prepare_load_profiles

.. autofunction:: flexgridpy.electrical_models.power_flow.load_input.prepare_custom_load_profiles

Example
-------

.. code-block:: python

   # After solving the OPF model:
   df_opf = mgr.results.wrapper_var_results()
   pp.runpp(net)
   df_pf = net.res_bus
   mgr.compare_results(df_opf, df_pf, tol=1e-4)
