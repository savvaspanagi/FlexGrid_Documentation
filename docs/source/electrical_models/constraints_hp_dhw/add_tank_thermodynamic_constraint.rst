add_tank_thermodynamic_constraint
==================================

Description
-----------

Adds the **stirred-tank DHW** thermodynamic constraint relating tank temperature
:math:`T_\text{tank}`, thermal input :math:`Q_\text{tank}`, heat loss, and hot
water demand.

Mathematical Formulation
------------------------

.. math::

   Q_{\text{tank},t} = \frac{T_{\text{tank},t+1} - T_{\text{tank},t}}{\Delta t \cdot 3600}
     \cdot C_\text{tank}
     + \frac{T_{\text{tank},t} - T_{\text{surr},t}}{R_\text{tank}}
     + Q_{\text{demand},t}

where:

* :math:`C_\text{tank}` — thermal capacitance of the water tank (J/K)
* :math:`R_\text{tank}` — thermal resistance to surroundings (K/W)
* :math:`Q_{\text{demand},t}` — hot water draw profile (kW)

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``Ttank``
     - Tank temperature variable (°C)
   * - ``Q_tank``
     - Thermal power delivered to tank (kW)
   * - ``Tsurr``
     - Surrounding/ambient temperature parameter
   * - ``Q_demand``
     - DHW demand profile parameter
   * - ``Q_dynamic_prefix_name``
     - Constraint group name

API Reference
-------------

.. autofunction:: flexgridpy.electrical_models.constraints.dhw.stirred_tank_thermodynamic_constr.add_tank_thermodynamic_constraint

Manager Wrapper
---------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.add_tank_thermodynamic_constraint

Example
-------

.. code-block:: python

   mgr.initialize_tank_params()
   mgr.dhw_profile_param()
   mgr.initialize_tank_variables()
   mgr.add_tank_thermodynamic_constraint(
       Ttank=mgr.model.Ttank,
       Q_tank=mgr.model.Qtank,
       Tsurr=mgr.model.Tsurr,
       Q_demand=mgr.model.Q_demand,
       Q_dynamic_prefix_name="TankDynamics",
   )
