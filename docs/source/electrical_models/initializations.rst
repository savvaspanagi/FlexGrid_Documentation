Initializations
===============

Helper classes for converting pandapower data into per-unit DataFrames and for
generating standard EV charging profiles.

AdditionalData
--------------

Converts the pandapower ``net`` into per-unit DataFrames compatible with the
optimization model.

.. autoclass:: flexgridpy.electrical_models.initializations.additional_data.AdditionalData
   :members:
   :undoc-members: False
   :show-inheritance:

Parameter DataFrame Utilities
-----------------------------

.. autoclass:: flexgridpy.electrical_models.initializations.parameter_df.parameter_df
   :members:
   :undoc-members: False
   :show-inheritance:

Result DataFrame Utilities
--------------------------

.. autoclass:: flexgridpy.electrical_models.initializations.var_results_df.var_results_df
   :members:
   :undoc-members: False
   :show-inheritance:

EV Profile Generation
---------------------

.. autofunction:: flexgridpy.electrical_models.initializations.ev_conv_profiles.generate_conventional_ev_profiles

Flexibility Plotting
--------------------

.. autofunction:: flexgridpy.electrical_models.plot.plot_flex.results_flexibility_plot
