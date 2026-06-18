Weather Data
============

Fetch outdoor temperature and global horizontal irradiance (GHI) from the
Open-Meteo API for model training and simulation.

Forecast Temperature
--------------------

.. autofunction:: flexgridpy.thermal_models.OpenMeteo.openMeteo.get_forecast_temperature_data

Historic Temperature
--------------------

.. autofunction:: flexgridpy.thermal_models.OpenMeteo.openMeteo.get_historic_temperature_data

Historic GHI
------------

.. autofunction:: flexgridpy.thermal_models.OpenMeteo.openMeteo.get_historic_ghi

Forecast GHI
------------

.. autofunction:: flexgridpy.thermal_models.OpenMeteo.openMeteo.get_forecast_ghi

Example
-------

.. code-block:: python

   from flexgridpy.thermal_models.OpenMeteo.openMeteo import get_historic_temperature_data

   df_temp = get_historic_temperature_data(
       lat=34.68, lon=33.04,
       start_date="2024-01-01", end_date="2024-01-31"
   )
