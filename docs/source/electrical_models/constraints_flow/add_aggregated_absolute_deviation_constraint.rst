add_aggregated_absolute_deviation_constraint
============================================

Function
--------

.. code-block:: python

   add_aggregated_absolute_deviation_constraint(manager, constraint_name_prefix, nominal_var, scenario_var, plus_deviation_var, minus_deviation_var, scenario_set, bus_set)

**Module:** ``flexgridpy.electrical_models.constraints.complex.absolute_deviation``

Manager Method
--------------

.. code-block:: python

   mgr.add_aggregated_absolute_deviation_constraint(...)

Adds aggregated absolute deviation constraints.

Example
-------

.. code-block:: python

   mgr.add_aggregated_absolute_deviation_constraint()
