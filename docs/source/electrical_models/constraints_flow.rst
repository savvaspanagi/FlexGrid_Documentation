Flow & Line Constraints
=======================

Current flow, line losses, and amplitude limit constraints for AC networks.

Current Flow
------------

.. autofunction:: flexgridpy.electrical_models.constraints.flow.current_constr.add_real_current_flow_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.flow.current_constr.add_reactive_current_flow_constraint

Line Losses
-----------

.. autofunction:: flexgridpy.electrical_models.constraints.line.line_constr.add_line_flow_losses_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.line.line_constr.add_line_flow_amplitude_losses_constraint

Amplitude Constraints
---------------------

.. autofunction:: flexgridpy.electrical_models.constraints.complex.ampl_constr.add_twoport_amplitude_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.complex.ampl_constr.add_oneport_amplitude_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.complex.ampl_constr.add_twoport_amplitude_limit_constraint

Absolute Deviation
------------------

.. autofunction:: flexgridpy.electrical_models.constraints.complex.absolute_deviation.add_absolute_deviation_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.complex.absolute_deviation.add_aggregated_absolute_deviation_constraint
