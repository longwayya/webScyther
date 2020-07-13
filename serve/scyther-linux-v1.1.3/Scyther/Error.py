#!/usr/bin/python
"""
	Scyther : An automatic verifier for security protocols.
	Copyright (C) 2007-2013 Cas Cremers

	This program is free software; you can redistribute it and/or
	modify it under the terms of the GNU General Public License
	as published by the Free Software Foundation; either version 2
	of the License, or (at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program; if not, write to the Free Software
	Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

#
# Scyther interface error classes
#

#---------------------------------------------------------------------------

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class ScytherError(Error):
    """Exception raised for errors generated by the backend

    Attributes:
        errorlist -- list of error lines are retrieved from the
        backend
    """

    def __init__(self, errorlist,filenames=None,options=None):
        self.errorlist = errorlist
        self.filenames = filenames
        self.options = options

    def __str__(self):
        s = "Scyther backend reported errors"
        if len(self.filenames) == 0:
            s = s + " for unknown files."
        if len(self.filenames) == 1:
            s = s + " for file %s" % (self.filenames)
        if len(self.filenames) > 1:
            s = s + " for files %s" % (self.filenames)
        s = s + "\n"
        s = s + "Options: '%s'\n\n" % (self.options)
        S = s + "Error details:\n"
        s = s + "\n".join(self.errorlist)
        return s

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class BinaryError(Error):
    """Raised when the Scyther executable is not found.

    Attributes:
        file -- file location at which we should have been able to find it.
    """

    def __init__(self, file):
        self.file = file

    def __str__(self):
        return "Could not find Scyther executable at '%s'" % (self.file)


class NoBinaryError(Error):
    """Raised when the Scyther executable is not defined.

    Attributes:
        None.
    """

    def __str__(self):
        return "Scyther class attribute 'program' was not defined."


class UnknownPlatformError(Error):
    """Raised when the platform is not supported yet.

    Attributes:
        platform -- string describing the platform.
    """

    def __init__(self, platform):
        self.platform = platform

    def __str__(self):
        return "The %s platform is currently unsupported." % self.platform

class StringListError(Error):
    """Raised when the a string should be a list of strings or a string

    Attributes:
        obj -- object that did not fit
    """

    def __init__(self, obj):
        self.obj = obj

    def __str__(self):
        return "Got '%s', which is type '%s' instead of a (list of) string." % (self.obj, type(self.obj))

# vim: set ts=4 sw=4 et list lcs=tab\:>-: