#    This file is part of the Minecraft Overviewer.
#
#    Minecraft Overviewer is free software: you can redistribute it and/or
#    modify it under the terms of the GNU General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or (at
#    your option) any later version.
#
#    Minecraft Overviewer is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
#    Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with the Overviewer.  If not, see <http://www.gnu.org/licenses/>.

import socket
#from enum import Enum
import struct
import select

class RConException(Exception):
    def __init__(self, request_id, reason):
        self.request_id = request_id
        self.reason = reason

    def __str__(self):
        return ("Failed RCon request with request ID %d, reason %s" %
                (self.request_id, self.reason))

# In D, enums are just that, enums. They're a group of named constants,
# sometimes with a tag, sometimes anonymous.
# In Python, Enums use the same syntax as class objects that derive from
# the "Enum" base class, even though they are not normal python classes
# and work as singletons anyway, but instead of using a different syntax,
# Python instead decided to have a chapter in their docs about how Enums
# are different from regular classes while looking exactly the same.
# You can look at said document of failure right here:
# https://docs.python.org/3/library/enum.html#how-are-enums-different
#
# "D has too much shit going on for me" -- agrif, 2014
#
# Fortunately, we're not allowed to use Enums in Python 2.

#class RConType(Enum):
#    command = 2
#    login = 3


class RConConnection():
    rid = 0

    def __init__(self, target, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((target, port))

    def send(self, t, payload):
        self.rid = self.rid + 1
        header = struct.pack("<iii",
                len(payload) + 4 + 4 + 2,    # rid, type and padding
                self.rid,
                t)
        data = header + payload + '\x00\x00'
        self.sock.send(data)


        toread = select.select([self.sock], [], [], 30)

        if not toread:
            raise RConException(self.rid, "Request timed out.")

        res_len, res_id, res_type = struct.unpack("<iii", self.sock.recv(12))
        res_data = self.sock.recv(res_len - 4 - 4)
        res_data = res_data[:-2]
        
        if res_id == -1:
            if t == 3:
                raise RConException(self.rid, "Login failed.")
            else:
                raise RConException(self.rid, "Request failed due to invalid login.")
        elif res_id != self.rid:
            raise RConException(self.rid,
                                "Received unexpected response number: %d" % res_id)
        
        return res_data
        

                
    def login(self, password):
        self.send(3, password)

    def command(self, com, args):
        self.send(2, com + " " + args)
        
    def close(self):
        self.sock.close()
