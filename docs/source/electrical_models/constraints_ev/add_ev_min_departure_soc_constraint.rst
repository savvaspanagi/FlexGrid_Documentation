add_ev_min_departure_soc_constraint
====================================

Function
--------

.. code-block:: python

   add_ev_min_departure_soc_constraint(manager, name_prefix)

**Module:** ``flexgridpy.electrical_models.constraints.ev.ev_min_soc_cons``

.. code-block:: python

   add_ev_min_custom_departure_soc_constraint(manager, custom_min_soc_percentage, name_prefix)

**Module:** ``flexgridpy.electrical_models.constraints.ev.ev_min_soc_cons``

.. code-block:: python

   add_ev_min_custom_departure_soc_stochastic_constraint(manager, custom_min_soc_percentage, name_prefix)

**Module:** ``flexgridpy.electrical_models.constraints.ev.ev_min_soc_cons``

Manager Method
--------------

.. code-block:: python

   mgr.add_ev_min_departure_soc_constraint(...)

Description
-----------

Ensures the EV battery has sufficient energy at each **departure event** to meet
the minimum required SOC before leaving.

Mathematical Formulation
------------------------

At departure time :math:`t = t_\text{dep}^x`:

.. math::

   E_{i,t} \geq E_{i}^\min_\text{dep}

where :math:`E_{i}^\min_\text{dep}` is derived from the minimum departure SOC
percentage and battery capacity.

Variants
--------

* ``add_ev_min_departure_soc_constraint`` — uses default minimum departure SOC
* ``add_ev_min_custom_departure_soc_constraint`` — custom SOC percentage per EV
* ``add_ev_min_custom_departure_soc_stochastic_constraint`` — scenario-indexed version
