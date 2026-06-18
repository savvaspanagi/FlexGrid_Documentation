Parameters
==========

Parameters hold fixed input data in the Pyomo model: network impedances, load
profiles, DER limits, EV characteristics, HP COP curves, and electricity prices.

All parameters are registered via ``manager.register_parameter(name, param)`` and
can be inspected with ``manager.list_parameters()``.

.. toctree::
   :maxdepth: 1

   parameters/line_param
   parameters/load_profile_param
   parameters/transformer_param
   parameters/alpha_bfm_param
   parameters/der_profile_param
   parameters/initialize_ev_params
   parameters/initialize_ev_char_params
   parameters/initialize_hp_params
   parameters/enviroment_profile_param
   parameters/price_profile_param
   parameters/initialize_tank_params
   parameters/add_stochastic_probabilities
