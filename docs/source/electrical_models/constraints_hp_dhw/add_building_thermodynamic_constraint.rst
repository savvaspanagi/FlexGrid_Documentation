add_building_thermodynamic_constraint
======================================

Description
-----------

Adds the **3R2C building thermodynamic** constraints coupling indoor temperature
:math:`T_\text{in}`, envelope temperature :math:`T_e`, space heating power
:math:`Q_\text{sh}`, outdoor temperature :math:`T_\text{out}`, and solar
irradiance :math:`Q_\text{sol}`.

Mathematical Formulation (Indoor Air)
--------------------------------------

.. math::

   Q_{\text{sh},t} = \frac{T_{\text{in},t+1} - T_{\text{in},t}}{\Delta t \cdot 3600}
     \cdot \frac{C_\text{in}}{f_h}
     - \frac{T_{e,t} - T_{\text{in},t}}{R_{\text{in,e}} / f_h}
     - \frac{T_{\text{out},t} - T_{\text{in},t}}{R_{\text{in,a}} \cdot f_h}
     - \frac{A_\text{in} \cdot Q_{\text{sol},t}}{f_h}

Mathematical Formulation (Envelope)
-----------------------------------

.. math::

   T_{e,t+1} = T_{e,t} + \Delta t \cdot 3600 \cdot \left(
     \frac{T_{\text{in},t} - T_{e,t}}{C_e R_{\text{in,e}}}
     + \frac{T_{\text{out},t} - T_{e,t}}{C_e R_{e,a}}
     + \frac{(1-f_h)\,Q_{\text{sh},t}}{C_e}
     + \frac{A_e \cdot Q_{\text{sol},t}}{C_e}
   \right)

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``Tin``, ``Te``
     - Indoor and envelope temperature variables
   * - ``Qsh``
     - Space heating thermal power variable
   * - ``Tout``, ``Qsol``
     - Outdoor temperature and solar irradiance parameters
   * - ``Q_dynamic_prefix_name``
     - Name for indoor air dynamics constraint
   * - ``Te_dynamic_prefix_name``
     - Name for envelope dynamics constraint

RC Parameters
-------------

Resistances :math:`R_{\text{in,e}}, R_{\text{in,a}}, R_{e,a}` and capacitances
:math:`C_\text{in}, C_e` are obtained from tuned grey-box models
(:doc:`../../building_modeling/temperature_tuning`).

API Reference
-------------

.. autofunction:: flexgridpy.electrical_models.constraints.hp.building_3R2C_thermodynamic_constr.add_building_thermodynamic_constraint

Manager Wrapper
---------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.add_building_thermodynamic_constraint

Example
-------

.. code-block:: python

   mgr.initialize_hp_params()
   mgr.enviroment_profile_param()
   mgr.initialize_hp_variables()
   mgr.initialize_building_variables()
   mgr.add_building_thermodynamic_constraint(
       Tin=mgr.model.Tin,
       Te=mgr.model.Te,
       Qsh=mgr.model.Qsh,
       Tout=mgr.model.Tout,
       Qsol=mgr.model.Qsol,
       Q_dynamic_prefix_name="BuildingQ",
       Te_dynamic_prefix_name="BuildingTe",
   )
