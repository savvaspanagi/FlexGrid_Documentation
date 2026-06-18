Building Modeling Overview
==========================

The thermal modeling pipeline in FlexGridPy follows three stages:

1. **Data preparation** — split measured time-series into train/validation/test sets.
2. **Parameter tuning** — fit grey-box RC model parameters (R, C values) via Pyomo optimization.
3. **Simulation** — forward-simulate indoor temperature or heating power with fitted parameters.

Supported RC model types include **1R1C**, **2R2C**, **3R2C**, and **4R3C** variants.

Typical Workflow
----------------

.. code-block:: python

   from flexgridpy.thermal_models.RC_Model.split_dataset import split_dataset
   from flexgridpy.thermal_models.RC_Model.t_models_train import train_greybox_t_model
   from flexgridpy.thermal_models.RC_Model.t_model_simulate import simulate_Tin

   train_df, val_df, test_df = split_dataset(df, train_days=5, val_days=2, test_days=2)

   bounds = {"Rie": (0.001, 0.1), "Rea": (0.001, 0.1), "Ci": (1e5, 1e7)}
   model, params, init, trials = train_greybox_t_model(
       train_df, model_type="2R2C_A", bounds=bounds, deltaT=3600, num_trials=10
   )

   Tin_sim = simulate_Tin(test_df, params, model_type="2R2C_A", deltaT=3600)

Integration with Electrical Models
----------------------------------

After tuning, the fitted R/C parameters can be passed to the electrical
optimization model via :func:`~flexgridpy.electrical_models.parameters.hp_param_fun.initialize_hp_params`
and :func:`~flexgridpy.electrical_models.constraints.hp.building_3R2C_thermodynamic_constr.add_building_thermodynamic_constraint`.
