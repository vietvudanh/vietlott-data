"""
Backward-compatibility shim.

``PredictModel`` now lives in ``machine_learning.strategies.base``.
This module re-exports it so that any existing imports continue to work.
"""

from machine_learning.strategies.base import PredictModel  # noqa: F401

__all__ = ["PredictModel"]
