# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

import frappe
from frappe.model.document import Document


class WorkflowDocumentState(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		allow_edit: DF.Link
		doc_status: DF.Literal["0", "1", "2"]
		is_optional_state: DF.Check
		message: DF.Text | None
		next_action_email_template: DF.Link | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		state: DF.Link
		update_field: DF.Literal
		update_value: DF.Data | None
	# end: auto-generated types
	pass
