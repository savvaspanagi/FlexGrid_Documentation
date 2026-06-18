check_socp_exactness
====================



Function
--------

.. autofunction:: flexgridpy.electrical_models.constraints.pf.distflow_wo_shunt_constr.check_socp_exactness

Manager Method
--------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.check_socp_exactness

Description
-----------

After solving a DistFlow SOCP problem, checks whether the SOCP relaxation is
**exact** (tight) for each branch and time step.

Mathematical Criterion
----------------------

For each branch :math:`(i,j)` and time :math:`t`, computes:

.. math::

   \text{gap}_{ij,t} = \ell_{ij,t}\,v_{i,t} - \left(P_{ij,t}^2 + Q_{ij,t}^2\right)

If :math:`|\text{gap}_{ij,t}| > \text{tol}` for any branch, the SOCP relaxation
is not exact and the solution may not be physically feasible for the original
non-convex problem.

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Argument
     - Description
   * - ``manager``
     - Manager instance (for accessing solved variable values)
   * - ``pline_var``, ``qline_var``, ``current_var``, ``voltage_var``
     - Solved Pyomo variables
   * - ``branch_set``, ``time_set``
     - Sets to check
   * - ``tol`` (float, default 1e-4)
     - Tolerance for exactness gap

Returns
-------

List of violations ``((i, j, t), lhs, rhs, gap)`` for branches where the
relaxation is not tight.



Example
-------

.. code-block:: python

   violations = mgr.check_socp_exactness(
       mgr.model.pLine, mgr.model.qLine,
       mgr.model.line_curr, mgr.model.voltage,
       mgr.model.Slines, mgr.model.STimes, tol=1e-4,
   )
   if violations:
       print(f"SOCP not exact for {len(violations)} branch-time pairs")
