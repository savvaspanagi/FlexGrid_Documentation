Dataset Tools
=============

Utilities for splitting measured data and visualizing tuning results.

Split Dataset
-------------

.. autofunction:: flexgridpy.thermal_models.RC_Model.split_dataset.split_dataset

Plotting Utilities
------------------

.. autofunction:: flexgridpy.thermal_models.RC_Model.plot.plot_residual

.. autofunction:: flexgridpy.thermal_models.RC_Model.plot.plot_parameter_vs_rmse

.. autofunction:: flexgridpy.thermal_models.RC_Model.plot.plot_parameters_vs_rmse_multi

.. autofunction:: flexgridpy.thermal_models.RC_Model.plot.plot_model_validation

Example
-------

.. code-block:: python

   from flexgridpy.thermal_models.RC_Model.split_dataset import split_dataset

   train_df, val_df, test_df = split_dataset(
       df=measured_df,
       train_days=10,
       val_days=3,
       test_days=3,
   )

   print(f"Train: {len(train_df)} samples, Val: {len(val_df)}, Test: {len(test_df)}")
