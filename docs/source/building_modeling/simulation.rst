Simulation
==========

Forward simulation of indoor temperature and heating power using fitted RC
model parameters.

Simulate Indoor Temperature
-------------------------

.. autofunction:: flexgridpy.thermal_models.RC_Model.t_model_simulate.simulate_Tin

Simulate Heating Power
----------------------

.. autofunction:: flexgridpy.thermal_models.RC_Model.q_model_simulate.simulate_Qh

Example
-------

.. code-block:: python

   from flexgridpy.thermal_models.RC_Model.t_model_simulate import simulate_Tin

   Tin_simulated = simulate_Tin(
       df=test_df,
       parameters=best_params,
       model_type="2R2C_A",
       deltaT=3600,
   )

   import matplotlib.pyplot as plt
   plt.plot(test_df.index, test_df["Tin"], label="Measured")
   plt.plot(test_df.index, Tin_simulated, label="Simulated")
   plt.legend()
   plt.show()
