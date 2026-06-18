initialize_der_variables
========================



Function
--------

.. autofunction:: flexgridpy.electrical_models.variables.def_der_var.initialize_der_variables

.. autofunction:: flexgridpy.electrical_models.variables.def_der_var.initialize_der_stochastic_variables

Manager Method
--------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.initialize_der_variables

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
