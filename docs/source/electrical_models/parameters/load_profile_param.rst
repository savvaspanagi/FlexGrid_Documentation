load_profile_param
==================

Function
--------

.. code-block:: python

   load_profile_param(manager, profiles, load_p_name_prefix, load_q_name_prefix)

**Module:** ``flexgridpy.electrical_models.parameters.load_param_fun``

Manager Method
--------------

.. code-block:: python

   mgr.load_profile_param(...)

Description
-----------

Registers active (:math:`P`) and reactive (:math:`Q`) load profiles for each
load bus and time step. Profiles are converted to per-unit values.

Reactive load is computed with a fixed power factor:

.. math::

   Q_{j,t} = P_{j,t} \times 0.328684

(corresponding to :math:`\cos\varphi \approx 0.95`).

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``profiles`` (DataFrame)
     - Active power profiles. Columns must match ``SLoadbuses`` or be a single column broadcast to all buses.
   * - ``load_p_name_prefix`` (str)
     - Name for active load parameter (e.g. ``"Load_P"``)
   * - ``load_q_name_prefix`` (str)
     - Name for reactive load parameter (e.g. ``"Load_Q"``)

Per-Unit Conversion
-------------------

.. math::

   P_{j,t}^\text{pu} = \frac{P_{j,t}^\text{kW}}{1000 \times S_\text{base}}

Validation
----------

* ``profiles`` must be a pandas DataFrame or Series.
* Time index must match ``model.STimes`` exactly.
* If multi-column, columns must equal ``model.SLoadbuses``.


Example
-------

.. code-block:: python

   import pandas as pd

   profiles = pd.DataFrame(
       {bus: [100.0] * 24 for bus in mgr.model.SLoadbuses},
       index=range(24),
   )
   mgr.load_profile_param(profiles, "Load_P", "Load_Q")
