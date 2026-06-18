initialize_der_variables
========================

Function
--------

.. code-block:: python

   initialize_der_variables(manager, power_control_name_prefix, power_curtail_prefix, reactive_prefix_name)

**Module:** ``flexgridpy.electrical_models.variables.def_der_var``

.. code-block:: python

   initialize_der_stochastic_variables(manager, power_control_name_prefix, power_curtail_prefix, reactive_prefix_name)

**Module:** ``flexgridpy.electrical_models.variables.def_der_var``

Manager Method
--------------

.. code-block:: python

   mgr.initialize_der_variables(...)

Description
-----------

Creates active and reactive power dispatch variables for controllable DER
(static generators) at each DER bus and time step.

Variables Created
-----------------

.. math::

   0 \leq P_{j,t}^\text{DER} \leq \overline{P}_{j,t}^\text{DER}, \quad
   0 \leq Q_{j,t}^\text{DER} \leq \overline{Q}_{j,t}^\text{DER}


See Also
--------

* :doc:`../parameters/der_profile_param`
