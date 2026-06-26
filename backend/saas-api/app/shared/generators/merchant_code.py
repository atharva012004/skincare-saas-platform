"""
Merchant code generator.
"""

from __future__ import annotations

MERCHANT_CODE_PREFIX = "MER"
MERCHANT_CODE_WIDTH = 6


def generate_merchant_code(
    sequence: int,
) -> str:
    """
    Generate a merchant code.

    Example:
        1 -> MER000001
    """

    if sequence < 1:
        raise ValueError(
            "Sequence must be greater than zero.",
        )

    return f"{MERCHANT_CODE_PREFIX}" f"{sequence:0{MERCHANT_CODE_WIDTH}d}"
