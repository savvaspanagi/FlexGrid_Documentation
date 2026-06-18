add_stochastic_probabilities
============================

Function
--------

.. code-block:: python

   add_stochastic_probabilities(manager, stochastic_probabilities_prefix_name, stochastic_probabilities_values, set_values)

**Module:** ``flexgridpy.electrical_models.parameters.stochastic_param``

Manager Method
--------------

.. code-block:: python

   mgr.add_stochastic_probabilities(...)

Description
-----------

Registers scenario probability weights :math:`\pi_s` for stochastic optimization.
Probabilities must sum to 1.

.. math::

   \sum_{s \in \mathcal{S}} \pi_s = 1, \quad \pi_s \geq 0

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Argument
     - Description
   * - ``probabilities`` (list)
     - List of scenario probabilities, length = number of scenarios
   * - ``prefix`` (str)
     - Registered parameter name


Example
-------

.. code-block:: python

   mgr.add_stochastic_set("SScenarios", 3)
   mgr.add_stochastic_probabilities([0.5, 0.3, 0.2], "scenario_prob")
