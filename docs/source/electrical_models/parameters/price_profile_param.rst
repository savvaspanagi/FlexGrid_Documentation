price_profile_param
===================

Function
--------

.. code-block:: python

   price_profile_param(manager, data, price_profile_name_prefix)

**Module:** ``flexgridpy.electrical_models.parameters.price_profile_param``

.. code-block:: python

   price_profile_stochastic_param(manager, data, price_profile_name_prefix)

**Module:** ``flexgridpy.electrical_models.parameters.price_profile_param``

Manager Method
--------------

.. code-block:: python

   mgr.price_profile_param(...)

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
