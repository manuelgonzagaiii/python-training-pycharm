import unittest

# TODO(author): replace with real checks.
# Test focus: Assert OrderStatus.DRAFT.value == 'draft' and PaymentStatus.PARTIALLY_PAID.value == 'partially_paid' (proves _generate_next_value_ ran). Assert OrderStatus('CONFIRMED') is OrderStatus.CONFIRMED, OrderStatus('  shipped ') is OrderStatus.SHIPPED, and OrderStatus('void') is OrderStatus.CANCELLED (alias) — all via _missing_. Assert OrderStatus('bogus') raises ValueError and that the same lookup for a clean canonical value still works. Assert .label renders 'Partially Paid'. Assert is_terminal(): CANCELLED/SHIPPED True, DRAFT False; REFUNDED True, UNPAID False. Assert can_transition_to enforces the table: DRAFT->CONFIRMED True, DRAFT->SHIPPED False, SHIPPED->anything False (terminal). Assert that the transition table is not a member (it does not appear in list(OrderStatus) and len(OrderStatus) == 4). Optionally assert isinstance(OrderStatus.DRAFT, str) so the StrEnum contract is exercised.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
