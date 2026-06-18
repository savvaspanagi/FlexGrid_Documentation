der_profile_param
=================



Function
--------

.. autofunction:: flexgridpy.electrical_models.parameters.der_param_fun.der_profile_param

.. autofunction:: flexgridpy.electrical_models.parameters.der_param_fun.der_profile_stochastic_param

Manager Method
--------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.der_profile_param

Description
-----------

Registers maximum active and reactive power limits for controllable and
uncontrollable DER (static generators) at each bus and time step.

Parameters Registered
---------------------

**Controllable DER** (prefix arguments):

* ``pder_max_prefix`` — :math:`\overline{P}_{j,t}^\text{DER}` (p.u.)
* ``qder_max_prefix`` — :math:`\overline{Q}_{j,t}^\text{DER}` (p.u.)

**Uncontrollable RES** (fixed generation profiles):

* ``unc_pder_prefix`` — :math:`P_{j,t}^\text{RES}` (p.u.)
* ``unc_qder_prefix`` — :math:`Q_{j,t}^\text{RES}` (p.u.)

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``profiles`` (DataFrame)
     - Active power profiles per DER bus and time step
   * - ``pder_max_prefix``, ``qder_max_prefix``
     - Prefix names for controllable DER limits
   * - ``unc_pder_prefix``, ``unc_qder_prefix``
     - Prefix names for uncontrollable RES injection
