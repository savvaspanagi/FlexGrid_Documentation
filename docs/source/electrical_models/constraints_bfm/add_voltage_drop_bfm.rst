add_voltage_drop_bfm
=====================

Function
--------

.. code-block:: python

   add_voltage_drop_bfm(manager, line_set, line_reverse_set, voltage_var, p_line_var, p_reverse_line_par, q_line_var, q_reverse_line_par, current_line_var, curret_reverse_line_var, resistance_param, reactance_param, alpha_real, alpha_imag, name_prefix, name_reverse_prefix)

**Module:** ``flexgridpy.electrical_models.constraints.pf.BFM_wshunt_radial_constr``

Manager Method
--------------

.. code-block:: python

   mgr.add_voltage_drop_bfm(...)

Description
-----------

Adds the BFM **voltage drop equation** along each branch, including the
:math:`\alpha` coefficient for tap ratio and phase shift.

Mathematical Formulation
------------------------

.. math::

   |\alpha_{ij}|^2 \cdot v_{i,t} - v_{j,t} =
   2\left[\alpha_{ij}^R \left(r_{ij} P_{ij,t} + x_{ij} Q_{ij,t}\right)
        - \alpha_{ij}^I \left(r_{ij} Q_{ij,t} + x_{ij} P_{ij,t}\right)\right]
   - |z_{ij}|^2 \cdot \ell_{ij,t}

where :math:`|\alpha_{ij}|^2 = (\alpha_{ij}^R)^2 + (\alpha_{ij}^I)^2`.

Both forward and reverse line directions are constrained.

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Argument
     - Description
   * - ``line_set``, ``line_reverse_set``
     - Forward and reverse branch sets
   * - ``voltage_var``
     - Squared voltage :math:`v_{i,t}`
   * - ``p_line_var``, ``p_reverse_line_par``, ``q_line_var``, ``q_reverse_line_par``
     - Branch power flow variables
   * - ``current_line_var``, ``curret_reverse_line_var``
     - Squared current variables
   * - ``resistance_param``, ``reactance_param``
     - Line :math:`r_{ij}`, :math:`x_{ij}`
   * - ``alpha_real``, ``alpha_imag``
     - BFM :math:`\alpha` coefficients
   * - ``name_prefix``, ``name_reverse_prefix``
     - Constraint group names


See Also
--------

* :doc:`../parameters/alpha_bfm_param`
