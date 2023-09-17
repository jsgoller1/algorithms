"""
Could we use a state graph with transitions to manage parsing? Suppose each list 
represents a state with valid transitions from it; all others are invalid. Go char by char
transitioning from state to state. If we cannot transition, return false. If we reach the last
character of the string, return true. 

At any point in our string, we could see:
- a to z, A to Z
- 0 to 9
- + or -
- . 

During traversal we also keep track of:
- Seen a . already (only one allowed)
- Seen an "e" already

Init:
    - digit: digit
    - +/-: +/-
    - .: .

Digit:
    - digit -> digit
    - . -> . (allowed if never seen before)
    - e: allowed if never seen it or . before -> e

-/+:
    - digit: -> digit
    - .: -> .

.:
    - digit: digit

e: 
    - digit: digit
"""
from string import digits
from collections import namedtuple


ParsingState = namedtuple("ParsingState", ["seen_decimal", "seen_scientific_e", "seen_digit"])


class ParsingGraphNode:
    def transition(self, char: str, state: ParsingState):
        if char in digits:
            return self.digit_transition(state)
        elif char in ["-", "+"]:
            return self.plus_minus_transition(state)
        elif char == ".":
            return self.decimal_transition(state)
        elif char in ["E", "e"]:
            return self.scientific_e_transition(state)
        return None, state

    def digit_transition(self, state: ParsingState):
        return None, state

    def plus_minus_transition(self, state: ParsingState):
        return None, state

    def decimal_transition(self, state: ParsingState):
        return None, state

    def scientific_e_transition(self, state: ParsingState):
        return None, state

    def termination_allowed(self, state: ParsingState):
        return False


class InitNode(ParsingGraphNode):
    """
    - digit: digit
    - +/-: +/-
    - .: .
    """

    def digit_transition(self, state: ParsingState):
        return DigitNode(), ParsingState(state.seen_decimal, state.seen_scientific_e, True)

    def plus_minus_transition(self, state: ParsingState):
        return PlusMinusNode(), state

    def decimal_transition(self, state: ParsingState):
        if not state.seen_decimal:
            return DecimalNode(), ParsingState(True, state.seen_scientific_e, state.seen_digit)
        else:
            return None, state

    def termination_allowed(self, state: ParsingState):
        return True


class DigitNode(ParsingGraphNode):
    """
    Digit:
        - digit -> digit
        - . -> . (allowed if never seen before)
        - e: allowed if never seen it or . before -> e
    """

    def digit_transition(self, state: ParsingState):
        return DigitNode(), ParsingState(state.seen_decimal, state.seen_scientific_e, True)

    def decimal_transition(self, state: ParsingState):
        if not state.seen_decimal and not state.seen_scientific_e:
            return DecimalNode(), ParsingState(True, state.seen_scientific_e, state.seen_digit)
        else:
            return None, state

    def scientific_e_transition(self, state: ParsingState):
        if not state.seen_scientific_e:
            return ScientificENode(), ParsingState(state.seen_decimal, True, state.seen_digit)
        else:
            return None, state

    def termination_allowed(self, state: ParsingState):
        return True


class PlusMinusNode(ParsingGraphNode):
    """
    -/+:
        - digit: -> digit
        - .: -> .
    """

    def digit_transition(self, state: ParsingState):
        return DigitNode(), ParsingState(state.seen_decimal, state.seen_scientific_e, True)

    def decimal_transition(self, state: ParsingState):
        # If the +/- followed an e, we cannot go to a decimal after
        if not state.seen_decimal and not state.seen_scientific_e:
            return DecimalNode(), ParsingState(True, state.seen_scientific_e, state.seen_digit)
        else:
            return None, state


class DecimalNode(ParsingGraphNode):
    """
    - digit: digit
    """

    def digit_transition(self, state: ParsingState):
        return DigitNode(), ParsingState(state.seen_decimal, state.seen_scientific_e, True)

    def scientific_e_transition(self, state: ParsingState):
        if state.seen_digit and not state.seen_scientific_e:
            return ScientificENode(), ParsingState(state.seen_decimal, True, state.seen_digit)
        else:
            return None, state

    def termination_allowed(self, state: ParsingState):
        return state.seen_digit


class ScientificENode(ParsingGraphNode):
    """
    - digit: digit
    """

    def digit_transition(self, state: ParsingState):
        return DigitNode(), ParsingState(state.seen_decimal, state.seen_scientific_e, True)

    def plus_minus_transition(self, state: ParsingState):
        return PlusMinusNode(), state


class Solution:
    def isNumber(self, s: str) -> bool:
        parsing_node = InitNode()
        parsing_state = ParsingState(False, False, False)
        for c in s:
            parsing_node, parsing_state = parsing_node.transition(c, parsing_state)
            if not (parsing_node):
                return False
        return parsing_node.termination_allowed(parsing_state)


s = Solution()
cases = [
    ("", True),
    ("1", True),
    ("11111", True),
    ("+11111", True),
    ("-11111", True),
    ("1.1", True),
    ("-1.1e15", True),
    ("3.", True),
    (".3", True),
    ("46.e3", True),
    ("005047e+6", True)

    ("--", False),
    ("-1-1111", False),
    ("e1111", False),
    ("-+11", False),
    ("garbage", False),
    ("1ee1.56", False),
    ("..56", False),
    (".56.", False),
    (".", False),
    ("e", False),
    ("0e", False),
    ("6e6.5", False)  # this is wrong; validly represents 6*10^6.5
]

for expr, expected in cases:
    actual = s.isNumber(expr)
    try:
        assert actual == expected
    except AssertionError:
        print(f"{expr}: {actual} != {expected}")
        raise
    except:
        print(f"expression: {expr}")
        raise
