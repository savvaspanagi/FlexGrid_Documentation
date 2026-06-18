add_absolute_deviation_constraint
=================================

Function
--------

.. code-block:: python

   add_absolute_deviation_constraint(manager, constraint_name_prefix, nominal_var, scenario_var, plus_deviation_var_name, minus_deviation_var_name, bus_set, time_set, scenario_set)

**Module:** ``flexgridpy.electrical_models.constraints.complex.absolute_deviation``

Manager Method
--------------

.. code-block:: python

   mgr.add_absolute_deviation_constraint(...)

Adds absolute deviation constraints for stochastic variables.

Example
-------

.. code-block:: python

   mgr.add_absolute_deviation_constraint()
