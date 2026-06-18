add_ev_soc_constraint
=====================

Description
-----------

Adds the **EV state-of-charge (SoC) dynamics** constraint. The battery energy
evolves with charging power and is reduced at trip departure events.

Mathematical Formulation
------------------------

At :math:`t = 0`:

.. math::

   E_{i,0} = E_{i,0}^\text{init} + p_{i,0}^\text{ch} \cdot \Delta t

For regular time steps:

.. math::

   E_{i,t} = E_{i,t-1} + p_{i,t}^\text{ch} \cdot \Delta t

At arrival time :math:`t = t_\text{arr}^x - 1` (before trip :math:`x`):

.. math::

   E_{i,t} = E_{i,t-1} - E_{i,x}^\text{trip}

where :math:`\Delta t =` ``manager.delta`` (hours) and :math:`p_{i,t}^\text{ch}` is the
EV charging power variable.

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Argument
     - Description
   * - ``name_prefix`` (str)
     - Constraint group name (e.g. ``"EV_SOC"``)

Required Parameters
-------------------

* ``EVinit_SOC`` — initial energy (from :doc:`../parameters/initialize_ev_params`)
* ``ev_arrival_time_param``, ``EV_trip_energy_needs_param`` (from :doc:`../parameters/initialize_ev_char_params`)
* ``pEVch`` — charging power variable

API Reference
-------------

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_soc_cons.add_ev_soc_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_soc_cons.add_ev_soc_constraint_stochastic

Manager Wrapper
---------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.add_ev_soc_constraint

Example
-------

.. code-block:: python

   mgr.initialize_ev_params(...)
   mgr.initialize_ev_char_params(...)
   mgr.initialize_ev_variables()
   mgr.add_ev_soc_constraint("EV_SOC")
