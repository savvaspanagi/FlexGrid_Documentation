alpha_bfm_param
===============

Description
-----------

Registers the BFM (Branch Flow Model) :math:`\alpha` coefficients used in the
voltage drop equations. The complex coefficient :math:`\alpha_{ij} = \alpha_{ij}^R + j\alpha_{ij}^I`
accounts for the tap ratio and phase shift of the branch.

Parameters Registered
---------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Prefix
     - Content
   * - ``alpha_real_prefix``
     - :math:`\alpha_{ij}^R = |\alpha_{ij}|^2` real component
   * - ``alpha_imag_prefix``
     - :math:`\alpha_{ij}^I` imaginary component

Required Before
---------------

Call this before adding BFM voltage-drop constraints
(:doc:`../constraints_bfm/add_voltage_drop_bfm`).

API Reference
-------------

.. autofunction:: flexgridpy.electrical_models.parameters.bfm_alpha_param_fun.alpha_bfm_param

Manager Wrapper
---------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.alpha_bfm_param
