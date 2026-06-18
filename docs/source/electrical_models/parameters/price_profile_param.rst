price_profile_param
===================

Description
-----------

Registers the time-varying electricity price profile :math:`\lambda_t` used in
the optimization objective (e.g. cost minimization or welfare maximization).

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Argument
     - Description
   * - ``price_profile`` (Series/DataFrame)
     - Price values per time step (e.g. €/MWh)
   * - ``price_prefix`` (str)
     - Registered parameter name

Objective Usage
---------------

The price enters the objective as:

.. math::

   \min \sum_{t \in \mathcal{T}} \lambda_t \left( \sum_j P_{j,t}^\text{grid} \right)

API Reference
-------------

.. autofunction:: flexgridpy.electrical_models.parameters.price_profile_param.price_profile_param

.. autofunction:: flexgridpy.electrical_models.parameters.price_profile_param.price_profile_stochastic_param

Manager Wrapper
---------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.price_profile_param
