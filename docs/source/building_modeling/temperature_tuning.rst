Temperature Model Tuning
========================

Fit grey-box RC models to measured indoor temperature data. The training
framework runs multiple random initializations and selects the best fit by RMSE.

Train Grey-Box Temperature Model
--------------------------------

.. autofunction:: flexgridpy.thermal_models.RC_Model.t_models_train.train_greybox_t_model

Build Grey-Box Temperature Model
--------------------------------

.. autofunction:: flexgridpy.thermal_models.RC_Model.t_models.build_greybox_t_model

Get Default Parameters & Bounds
-------------------------------

.. autofunction:: flexgridpy.thermal_models.RC_Model.t_models.get_t_model_parameters

Extract Fitted Parameters
-------------------------

.. autofunction:: flexgridpy.thermal_models.RC_Model.t_models.extract_t_model_parameters

Plot Temperature Comparison
---------------------------

.. autofunction:: flexgridpy.thermal_models.RC_Model.t_models.plot_t_model_temperature_comparison

Example
-------

.. code-block:: python

   from flexgridpy.thermal_models.RC_Model.t_models_train import train_greybox_t_model

   bounds = {
       "Rie": (0.001, 0.05),
       "Rea": (0.001, 0.05),
       "Ci": (1e5, 5e6),
       "Ce": (1e6, 1e8),
   }

   model, params, init, trials = train_greybox_t_model(
       train_df=train_df,
       model_type="2R2C_A",
       bounds=bounds,
       deltaT=3600,
       solver_name="ipopt",
       num_trials=20,
       show_plot=True,
       validation=True,
       val_df=val_df,
   )

   print(f"Best RMSE: {params['RMSE']:.4f}")
   print(f"Fitted Rie={params['Rie']:.6f}, Ci={params['Ci']:.0f}")

Supported Model Types
---------------------

- **1R1C** — Single-zone, 1 resistance, 1 capacitance
- **2R2C_A** — Two resistances, two capacitances
- **2R2C_B** — Alternative 2R2C topology
- **3R2C** — Three resistances, two capacitances
- **4R3C** — Four resistances, three capacitances
