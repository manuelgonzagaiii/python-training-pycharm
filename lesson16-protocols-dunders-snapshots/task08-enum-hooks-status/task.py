"""Customizing Enums: _missing_, _generate_next_value_, and member methods

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: In core/status.py (new module in the shared domain layer), define two StrEnums. Provide _generate_next_value_(name, start, count, last_values) BEFORE the members so auto() returns name.lower() (PaymentStatus.PARTIALLY_PAID -> 'partially_paid'). Members: OrderStatus = DRAFT/CONFIRMED/SHIPPED/CANCELLED, PaymentStatus = UNPAID/PARTIALLY_PAID/PAID/REFUNDED, all assigned auto(). Add a classmethod _missing_(cls, value) that, for str input, strips+lowercases and matches against each member's .value and .name (plus an _ALIASES dict, e.g. {'void':'cancelled','complete':'shipped'} for OrderStatus), returning the member or None. Add a label @property returning self.name.replace('_',' ').title(); an is_terminal() method (SHIPPED/CANCELLED, REFUNDED true); and can_transition_to(self, target) backed by a module-level _TRANSITIONS dict mapping each member to the frozenset of allowed next members. Keep the transition table as a plain module-level dict (NOT inside the class body) so it is not turned into an enum member. Provide a parse_status(raw, kind) helper that calls the right enum and lets ValueError propagate for unknown input.
"""

# Your code here.
