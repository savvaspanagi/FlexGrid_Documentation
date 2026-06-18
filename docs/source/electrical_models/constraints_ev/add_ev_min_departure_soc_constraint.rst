add_ev_min_departure_soc_constraint
====================================



Function
--------

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_min_soc_cons.add_ev_min_departure_soc_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_min_soc_cons.add_ev_min_custom_departure_soc_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_min_soc_cons.add_ev_min_custom_departure_soc_stochastic_constraint

Manager Method
--------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.add_ev_min_departure_soc_constraint

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
