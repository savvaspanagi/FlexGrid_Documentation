add_HP_operation_constraint
============================

Function
--------

.. code-block:: python

   add_HP_operation_constraint(manager, Qhp, php, qhp, COP_param, php_operation_prefix_name, qhp_operation_prefix_name, Qtank=None)

**Module:** ``flexgridpy.electrical_models.constraints.hp.hp_operation_constr``

Manager Method
--------------

.. code-block:: python

   mgr.add_HP_operation_constraint(...)

Description
-----------

Links heat-pump **thermal output** :math:`Q_\text{hp}` to **electrical consumption**
:math:`p_\text{hp}` via the COP curve.

Mathematical Formulation
------------------------

.. math::

   p_{\text{hp},t} = \frac{Q_{\text{hp},t}}{\text{COP}(\Delta T_t)}

where :math:`\Delta T_t = T_{\text{sink},t} - T_{\text{source},t}` and COP is a
regression function of the temperature lift (see
:class:`~flexgridpy.thermal_models.HP_Operation.hp_model.HeatPumpModel`).

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``Qhp``
     - Heat pump thermal power variable
   * - ``php``, ``qhp``
     - Electrical active/reactive power variables
   * - ``COP_param``
     - COP parameter or curve
   * - ``php_operation_prefix_name``, ``qhp_operation_prefix_name``
     - Constraint group names
   * - ``Qtank`` (optional)
     - Tank thermal power for DHW mode


Example
-------

.. code-block:: python

   mgr.add_HP_operation_constraint(
       Qhp=mgr.model.Qhp,
       php=mgr.model.php,
       qhp=mgr.model.qhp,
       COP_param=mgr.model.COP_param,
       php_operation_prefix_name="HP_P",
       qhp_operation_prefix_name="HP_Q",
   )
