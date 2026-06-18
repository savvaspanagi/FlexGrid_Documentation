initialize_ev_params
====================

Function
--------

.. code-block:: python

   initialize_ev_params(manager, min_ch_prefix_name, max_ch_prefix_name, EV_init_SOC_prefix_name, EV_end_SOC_prefix_name, EV_min_SOC_prefix_name, EV_max_SOC_prefix_name, EV_Ene_Capa_prefix_name)

**Module:** ``flexgridpy.electrical_models.parameters.ev_param_fun``

Manager Method
--------------

.. code-block:: python

   mgr.initialize_ev_params(...)

Description
-----------

Registers EV battery and charger parameters for each bus in ``SEVbuses``.

Parameters Registered
---------------------

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Prefix argument
     - Physical meaning
   * - ``min_ch_prefix_name``
     - Minimum charging power :math:`\underline{P}_\text{ch}` (p.u.)
   * - ``max_ch_prefix_name``
     - Maximum charging power :math:`\overline{P}_\text{ch}` (p.u.)
   * - ``EV_init_SOC_prefix_name``
     - Initial energy :math:`E_0 = EC \times SOC_0 / 100` (p.u.·h)
   * - ``EV_end_SOC_prefix_name``
     - Target energy at end of horizon :math:`E_\text{end}` (p.u.·h)
   * - ``EV_min_SOC_prefix_name``
     - Minimum allowed energy :math:`E_\min` (p.u.·h)
   * - ``EV_max_SOC_prefix_name``
     - Maximum allowed energy :math:`E_\max` (p.u.·h)
   * - ``EV_Ene_Capa_prefix_name``
     - Battery capacity :math:`EC` (p.u.·h)

Energy Conversion
---------------

SOC percentages from the input DataFrame are converted to energy:

.. math::

   E_0 = EC \times \frac{SOC_0}{100}

Arguments
---------

All seven prefix arguments are **required** strings naming the registered Pyomo
``Param`` objects.


Example
-------

.. code-block:: python

   mgr.anc_Vars.addEV(ev_dataframe)
   mgr.initialize_ev_params(
       min_ch_prefix_name="ev_min_ch_param",
       max_ch_prefix_name="ev_max_ch_param",
       EV_init_SOC_prefix_name="EVinit_SOC",
       EV_end_SOC_prefix_name="EVend_SOC_param",
       EV_min_SOC_prefix_name="EV_SoC_min_pref_param",
       EV_max_SOC_prefix_name="EV_SoC_max_param",
       EV_Ene_Capa_prefix_name="EV_capacity_param",
   )
