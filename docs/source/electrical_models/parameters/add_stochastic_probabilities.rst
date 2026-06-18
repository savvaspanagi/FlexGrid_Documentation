add_stochastic_probabilities
============================

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

API Reference
-------------

.. autofunction:: flexgridpy.electrical_models.parameters.stochastic_param.add_stochastic_probabilities

Manager Wrapper
---------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.add_stochastic_probabilities

Example
-------

.. code-block:: python

   mgr.add_stochastic_set("SScenarios", 3)
   mgr.add_stochastic_probabilities([0.5, 0.3, 0.2], "scenario_prob")
