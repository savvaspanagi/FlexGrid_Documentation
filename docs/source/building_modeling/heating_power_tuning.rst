Heating Power Model Tuning
==========================

Fit grey-box models to measured heating power (Qh) data. The Q-model captures
the relationship between outdoor temperature, solar irradiance, and heating demand.

Train Grey-Box Heating Power Model
----------------------------------

.. autofunction:: flexgridpy.thermal_models.RC_Model.q_model_train.train_greybox_q_model

Build Grey-Box Heating Power Model
----------------------------------

.. autofunction:: flexgridpy.thermal_models.RC_Model.q_models.build_greybox_q_model

Get Default Parameters & Bounds
-------------------------------

.. autofunction:: flexgridpy.thermal_models.RC_Model.q_models.get_q_model_parameters

Extract Fitted Parameters
-------------------------

.. autofunction:: flexgridpy.thermal_models.RC_Model.q_models.extract_q_model_parameters

Plot Power Comparison
-------------------

.. autofunction:: flexgridpy.thermal_models.RC_Model.q_models.plot_q_model_power_comparison

Ambience Profile Extraction
---------------------------

Simulate heating/cooling power for a target indoor temperature profile.

.. autofunction:: flexgridpy.thermal_models.Ambience_Models.q_model_profile_extraction.simulate_Qh_Ambience

Example
-------

.. code-block:: python

   from flexgridpy.thermal_models.RC_Model.q_model_train import train_greybox_q_model

   bounds = {"Rie": (0.001, 0.05), "Ci": (1e5, 5e6)}

   model, params, init, trials = train_greybox_q_model(
       train_df=train_df,
       model_type="1R1C",
       bounds=bounds,
       deltaT=3600,
       num_trials=15,
   )
