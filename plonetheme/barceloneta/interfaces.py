# -*- coding: utf-8 -*-
from plone.app.z3cform.interfaces import IPloneFormLayer
from plone.theme.interfaces import IDefaultPloneLayer


class IBarcelonetaLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer and a plone skin
       marker.
    """


class IBarcelonetaFormLayer(IPloneFormLayer):
    """Marker for plone.app.z3cform overrides
    """
