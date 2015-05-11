from variables import *
from arma_common import Assign, configure_arg

def Get(node):

    # Single argument
    if len(node) == 1:

        if node[0].type == "TYPE":
            return "%(name)s(%(0)s)"

        arg, dim = configure_arg(node[0], 0)
        if dim == 0:
            node.dim = 0

        return "vectorise(%(name)s)(" + arg + ")"


    # Double argument
    elif len(node) == 2:

        if "TYPE" in (node[0].type, node[1].type):
            return "%(name)s(", ", ", ")"

        arg0, dim0 = configure_arg(node[0], 0)
        arg1, dim1 = configure_arg(node[1], 1)

        # Configure dimensions
        if dim0:
            if dim1:
                node.dim = 3
            else:
                node.dim = 1
                arg1 = "span("+arg1+")"
        else:
            if dim1:
                node.dim = 2
                arg0 = "span("+arg0+")"
            else:
                node.dim = 0

        return "%(name)s(" + arg0 + ", " + arg1 + ")"


def Set(node):

    # Single argument
    if len(node) == 1:

        if node[0].type == "TYPE":
            return "%(name)s(", ", ", ")"

        arg, dim = configure_arg(node[0], 0)
        if dim == 0:
            node.dim = 0

        return "%(name)s(" + arg + ")"


    # Double argument
    elif len(node) == 2:

        if "TYPE" in (node[0].type, node[1].type):
            return "%(name)s(", ", ", ")"

        arg0, dim0 = configure_arg(node[0], 0)
        arg1, dim1 = configure_arg(node[1], 1)

        # Configure dimensions
        if dim0:
            if dim1:
                node.dim = 3
            else:
                node.dim = 1
                arg1 = "span("+arg1+")"
        else:
            if dim1:
                node.dim = 2
                arg0 = "span("+arg0+")"
            else:
                node.dim = 0

        return "%(name)s(" + arg0 + ", " + arg1 + ")"
