Parameters
==========

Parameters hold the fixed input data of the optimization model: network
impedances, load profiles, DER limits, EV characteristics, heat-pump COP
curves, electricity prices, and environment profiles.

Network Parameters
------------------

Line Parameters
~~~~~~~~~~~~~~~

.. autofunction:: flexgridpy.electrical_models.parameters.line_param_fun.line_param

Load Parameters
~~~~~~~~~~~~~~~

.. autofunction:: flexgridpy.electrical_models.parameters.load_param_fun.load_profile_param

Transformer Parameters
~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: flexgridpy.electrical_models.parameters.transformer_param_fun.transformer_param

.. autofunction:: flexgridpy.electrical_models.parameters.transformer_param_fun.transformer_nominal_power_param

BFM Parameters
~~~~~~~~~~~~~~

.. autofunction:: flexgridpy.electrical_models.parameters.bfm_alpha_param_fun.alpha_bfm_param

DER Parameters
--------------

.. autofunction:: flexgridpy.electrical_models.parameters.der_param_fun.der_profile_param

EV Parameters
-------------

.. autofunction:: flexgridpy.electrical_models.parameters.ev_param_fun.initialize_ev_params

.. autofunction:: flexgridpy.electrical_models.parameters.ev_char_param_fun.initialize_ev_char_params

.. autofunction:: flexgridpy.electrical_models.parameters.ev_soc_min_timeseries.initialize_ev_min_soc_timeseries

Heat Pump & Building Parameters
-------------------------------

.. autofunction:: flexgridpy.electrical_models.parameters.hp_param_fun.initialize_hp_params

.. autofunction:: flexgridpy.electrical_models.parameters.hp_param_fun.hp_flexibility_params

.. autofunction:: flexgridpy.electrical_models.parameters.enviroment_param.enviroment_profile_param

Tank & DHW Parameters
-----------------------

.. autofunction:: flexgridpy.electrical_models.parameters.tank_param_fun.initialize_tank_params

.. autofunction:: flexgridpy.electrical_models.parameters.tank_param_fun.tank_flexibility_params

.. autofunction:: flexgridpy.electrical_models.parameters.dhw_profile_param.dhw_profile_param

Price Parameters
----------------

.. autofunction:: flexgridpy.electrical_models.parameters.price_profile_param.price_profile_param

Stochastic Parameters
---------------------

.. autofunction:: flexgridpy.electrical_models.parameters.stochastic_param.add_stochastic_probabilities

.. autofunction:: flexgridpy.electrical_models.parameters.ev_char_param_fun.initialize_ev_char_stochastic_params

.. autofunction:: flexgridpy.electrical_models.parameters.hp_param_fun.initialize_hp_stochastic_params

.. autofunction:: flexgridpy.electrical_models.parameters.price_profile_param.price_profile_stochastic_param

.. autofunction:: flexgridpy.electrical_models.parameters.enviroment_param.enviroment_profile_stochastic_param

.. autofunction:: flexgridpy.electrical_models.parameters.der_param_fun.der_profile_stochastic_param
