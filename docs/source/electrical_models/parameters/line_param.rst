line_param
==========

Function
--------

.. code-block:: python

   line_param(manager, Y_bus_df, resist_prefix, react_prefix, adm_real_prefix, adm_img_prefix)

**Module:** ``flexgridpy.electrical_models.parameters.line_param_fun``

Manager Method
--------------

.. code-block:: python

   mgr.line_param(...)

Description
-----------

Registers per-unit line resistance :math:`R_{ij}`, reactance :math:`X_{ij}`, and
the full bus admittance matrix :math:`\mathbf{Y}_\text{bus}` as Pyomo parameters.
Values are extracted from ``anc_Vars.System_Data_Lines`` and the pre-computed
Y-bus matrix.

Parameters Registered
---------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Prefix argument
     - Pyomo Param
   * - ``resist_prefix``
     - :math:`R_{ij}` for each line :math:`(i,j) \in \mathcal{L}`
   * - ``react_prefix``
     - :math:`X_{ij}` for each line :math:`(i,j) \in \mathcal{L}`
   * - ``adm_real_prefix``
     - :math:`\Re\{Y_{ik}\}` — real part of Y-bus
   * - ``adm_img_prefix``
     - :math:`\Im\{Y_{ik}\}` — imaginary part of Y-bus

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``Y_bus_df`` (DataFrame)
     - Complex admittance matrix indexed by bus pairs
   * - ``resist_prefix`` (str)
     - Name for resistance parameter (e.g. ``"resistance_Parm"``)
   * - ``react_prefix`` (str)
     - Name for reactance parameter
   * - ``adm_real_prefix`` (str)
     - Name for real admittance matrix
   * - ``adm_img_prefix`` (str)
     - Name for imaginary admittance matrix

Per-Unit System
---------------

Line data are converted to per-unit when ``AdditionalData`` is created
(``mgr.anc_Vars``). ``line_param`` then reads the pre-computed p.u. values from
``System_Data_Lines`` and registers them as Pyomo parameters.

**System base** (from ``net.sn_mva`` and bus nominal voltages):

.. math::

   S_\text{base} &= \texttt{net.sn\_mva} \quad [\text{MVA}] \\
   Z_\text{base}(V) &= \frac{V_\text{base}^2}{S_\text{base}} \quad [\Omega], \quad V_\text{base} = \texttt{vn\_kv} \\
   I_\text{base}(V) &= \frac{S_\text{base} \cdot 10^6}{\sqrt{3}\, V_\text{base} \cdot 10^3 \cdot 10^3} \quad [\text{kA}] \\
   Y_\text{base} &= \frac{S_\text{base}}{V_\text{base}^2} \quad [\text{S}]

For each line, :math:`Z_\text{base}` and :math:`I_\text{base}` are taken from the
voltage level of the **from-bus** (``vn_kv``).

**Line series impedance** (``define_lines`` in ``additional_data.py``):

Let :math:`\ell` be ``length_km``, :math:`r'` = ``r_ohm_per_km``, :math:`x'` = ``x_ohm_per_km``:

.. math::

   R_{ij}^\text{pu} &= \frac{r' \cdot \ell}{Z_\text{base}(V_i)} \\
   X_{ij}^\text{pu} &= \frac{x' \cdot \ell}{Z_\text{base}(V_i)}

**Line shunt susceptance** (stored in ``System_Data_Lines['Y']``):

.. math::

   Y_{ij}^\text{pu} = \frac{2\pi f \cdot c_\text{nf} \cdot \ell \cdot 10^{-9}}{Y_\text{base}}

with :math:`f = 50` Hz and :math:`c_\text{nf}` = ``c_nf_per_km``.

**Y-bus matrix** (``build_ybus``): built in per-unit using the from-bus impedance base.
For a series admittance :math:`y = 1/(r + jx)` in Siemens:

.. math::

   y^\text{pu} = y \cdot Z_\text{base}(V_i)

Shunt line capacitance is added to the diagonal as :math:`y_\text{sh}^\text{pu}/2`.
Transformer contributions are also scaled to the system base inside ``build_ybus``.

``line_param`` registers :math:`R_{ij}^\text{pu}`, :math:`X_{ij}^\text{pu}` from
``System_Data_Lines`` and the real/imaginary parts of the pre-computed
:math:`\mathbf{Y}_\text{bus}` DataFrame.


Example
-------

.. code-block:: python

   from flexgridpy.electrical_models.admittance_matrix.makeYbus import makeYbus

   Y_bus = makeYbus(mgr.net, mgr.anc_Vars)
   mgr.line_param(
       Y_bus,
       resist_prefix="resistance_Parm",
       react_prefix="reactance_Parm",
       adm_real_prefix="admitt_mat_Parm_real",
       adm_img_prefix="admitt_mat_Parm_imag",
   )
