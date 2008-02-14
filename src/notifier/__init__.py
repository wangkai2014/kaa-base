# -*- coding: iso-8859-1 -*-
# -----------------------------------------------------------------------------
# __init__.py - Interface to kaa.notifier
# -----------------------------------------------------------------------------
# $Id$
#
# -----------------------------------------------------------------------------
# kaa.notifier - Mainloop and callbacks
# Copyright (C) 2005-2008 Dirk Meyer, Jason Tackaberry, et al.
#
# First Version: Dirk Meyer <dmeyer@tzi.de>
# Maintainer:    Dirk Meyer <dmeyer@tzi.de>
#                Jason Tackaberry <tack@urandom.ca>
#
# Please see the file AUTHORS for a complete list of authors.
#
# This library is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version
# 2.1 as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301 USA
#
# -----------------------------------------------------------------------------

# Import all classes, functions and decorators that are part of the API

# Callback classes
from callback import Callback, WeakCallback

# Signal and dict of Signals
from signals import Signal, Signals

# InProgress class
from async import TimeoutException, InProgress, InProgressCallback

# Thread callbacks, helper functions and decorators
from thread import MainThreadCallback, NamedThreadCallback, ThreadCallback, \
     is_mainthread, threaded, MAINTHREAD

# Timer classes and decorators
from timer import Timer, WeakTimer, OneShotTimer, WeakOneShotTimer, AtTimer, \
     OneShotAtTimer, timed, POLICY_ONCE, POLICY_MANY, POLICY_RESTART

# IO/Socket handling
from sockets import IOMonitor, WeakIOMonitor, Socket, IO_READ, IO_WRITE

# Event and event handler classes
from event import Event, EventHandler, WeakEventHandler

# coroutine decorator and helper classes
from coroutine import NotFinished, coroutine

# process management
from popen import Process
