add_stochastic_set
==================

Description
-----------

Adds a scenario-index set for stochastic / robust optimization. Each scenario
represents one realization of uncertain parameters (e.g. PV generation, EV
arrival times, electricity prices).

Mathematical Definition
-----------------------

.. math::

   \mathcal{S} = \{0, 1, \ldots, N_s - 1\}

where :math:`N_s` is the number of scenarios passed as ``stochastic_set_values``.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Argument
     - Description
   * - ``stochastic_set_name_prefix`` (str)
     - Name under which the set is registered (typically ``"SScenarios"``)
   * - ``stochastic_set_values`` (int)
     - Number of scenarios :math:`N_s`

API Reference
-------------

.. autofunction:: flexgridpy.electrical_models.sets.stochastic_set.add_stochastic_set

Manager Wrapper
---------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.add_stochastic_set

Example
-------

.. code-block:: python

   mgr.add_stochastic_set("SScenarios", 5)
   mgr.add_stochastic_probabilities([0.1, 0.2, 0.3, 0.2, 0.2])

See Also
--------

* :doc:`../parameters/add_stochastic_probabilities`
* :doc:`../constraints_stochastic`
