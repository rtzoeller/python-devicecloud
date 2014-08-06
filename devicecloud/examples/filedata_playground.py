# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2014 Etherios, Inc. All rights reserved.
# Etherios, Inc. is a Division of Digi International.
from getpass import getpass

from devicecloud import DeviceCloud
from devicecloud.filedata import fd_path, fd_name, fd_size, fd_type
from devicecloud.streams import DataPoint, NoSuchStreamException


def get_authenticated_dc():
    while True:
        user = raw_input("username: ")
        password = getpass("password: ")
        dc = DeviceCloud(user, password, base_url="https://test.idigi.com")
        if dc.has_valid_credentials():
            print ("Credentials accepted!")
            return dc
        else:
            print ("Invalid username or password provided, try again")


if __name__ == '__main__':
    dc = get_authenticated_dc()

    dc.filedata.write_file("/~/test_dir/", "test_file.txt", "Helllo, world!", "text/plain")

    query = None  # (fd_path == '/db/public/')
    for dirpath, directories, files in dc.filedata.walk():
        for fd_file in files:
            print fd_file

    print dc.filedata.get_filedata(
        (fd_type == "file") &
        (fd_size < 250) &
        (fd_name.like('%.txt'))
    )