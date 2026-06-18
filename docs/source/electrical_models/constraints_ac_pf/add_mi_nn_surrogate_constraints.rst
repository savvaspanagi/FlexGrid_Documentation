add_mi_nn_surrogate_constraints
===============================

Function
--------

.. code-block:: python

   add_mi_nn_surrogate_constraints(manager, nn_binary_var, nn_z_var, nn_h_var, W1, b1, W2, b2, X_mean, X_std, y_mean, y_std, load_p_param=None, load_q_param=None, pder_uncontr_param=None, qder_uncontr_param=None, pder_contr_var=None, qder_contr_var=None, ev_ch_p_var=None, ev_ch_q_var=None, p_hp_var=None, q_hp_var=None, name_prefix='mi_nn', M=1000.0, voltage_var=None, current_var=None, neurons_bus_mapping=None, neurons_line_mapping=None, min_voltage_only=False)

**Module:** ``flexgridpy.electrical_models.constraints.pf.mi_nn_surrogate``

Manager Method
--------------

.. code-block:: python

   mgr.add_mi_nn_surrogate_constraints(...)

Adds mixed-integer neural network surrogate constraints.

Example
-------

.. code-block:: python

   mgr.add_mi_nn_surrogate_constraints()
