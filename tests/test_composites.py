#!/usr/bin/env python
#
# License: BSD
#   https://raw.githubusercontent.com/stonier/py_trees/devel/LICENSE
#

##############################################################################
# Imports
##############################################################################

import py_trees
import py_trees.console as console

##############################################################################
# Logging Level
##############################################################################

py_trees.logging.level = py_trees.logging.Level.DEBUG
logger = py_trees.logging.Logger("Nosetest")

##############################################################################
# Tests
##############################################################################


def test_replacing_children():
    console.banner("Replacing Children")
    parent = py_trees.composites.Sequence(name="Parent")
    old_child = py_trees.behaviours.Success(name="Old Child")
    new_child = py_trees.behaviours.Success(name="New Child")
    parent.add_child(old_child)
    parent.replace_child(old_child, new_child)
    print("\n--------- Assertions ---------\n")
    print("old_child.parent is None")
    assert(old_child.parent is None)
    print("new_child.parent is parent")
    assert(new_child.parent is parent)

def test_removing_children():
    console.banner("Removing Children")
    parent = py_trees.composites.Sequence(name="Parent")
    child = py_trees.behaviours.Success(name="Child")
    print("\n--------- Assertions ---------\n")
    print("child.parent is None after removing by instance")
    parent.add_child(child)
    parent.remove_child(child)
    assert(child.parent is None)
    print("child.parent is None after removing by id")
    parent.add_child(child)
    parent.remove_child_by_id(child.id)
    assert(child.parent is None)
    print("child.parent is None after removing all children")
    parent.add_child(child)
    parent.remove_all_children()
    assert(child.parent is None)
