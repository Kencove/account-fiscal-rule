# Copyright (C) 2026 Kencove
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


def migrate(cr, version):
    """
    Remove old selection values for service_url field before converting
    from Selection to Char field type.
    """
    # Delete old selection values to prevent AttributeError during upgrade
    cr.execute(
        """
        DELETE FROM ir_model_fields_selection
        WHERE field_id IN (
            SELECT id FROM ir_model_fields
            WHERE model = 'avalara.salestax'
            AND name = 'service_url'
        )
        """
    )
