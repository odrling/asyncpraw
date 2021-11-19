"""Provide the Stylesheet class."""

from .base import AsyncPRAWBase


class Stylesheet(AsyncPRAWBase):
    """Represent a stylesheet.

    .. include:: ../../typical_attributes.rst

    ============== ============================================
    Attribute      Description
    ============== ============================================
    ``images``     A ``list`` of images used by the stylesheet.
    ``stylesheet`` The contents of the stylesheet, as CSS.
    ============== ============================================

    """
