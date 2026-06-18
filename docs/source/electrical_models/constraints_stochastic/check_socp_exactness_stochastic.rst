check_socp_exactness_stochastic
===============================

Function
--------

.. code-block:: python

   check_socp_exactness_stochastic(manager, pline_var, qline_var, current_var, voltage_var, branch_set, time_set, tol=0.0001)

**Module:** ``flexgridpy.electrical_models.constraints.pf.distflow_wo_shunt_stochastic_constr``

Manager Method
--------------

.. code-block:: python

   mgr.check_socp_exactness_stochastic(...)

Checks SOCP exactness for stochastic DistFlow.

Example
-------

.. code-block:: python

   mgr.check_socp_exactness_stochastic()
