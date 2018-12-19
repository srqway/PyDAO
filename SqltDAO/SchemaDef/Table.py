#!/usr/bin/env python3
#
# Author: Soft9000.com
# 2018/12/19: File created

# Mission: Manage the table-definition order
# Status: WORK IN PROGRESS

from collections import OrderedDict

class TableDef():
    ''' Basic table definitions. '''

    SupportedTypes = ("id", "text", "integer", "float")

    def __init__(self, name='Default'):
        self._name = TableDef.Normalize(name)
        self.fields = OrderedDict()
        self.add_field("ID", "integer")

    def get_table_name(self):
        ''' Query the table name. '''
        return self._name

    def set_table_name(self, name):
        ''' Change the table name. '''
        self._name = TableDef.Normalize(name)

    def add_field(self, name, ztype):
        ''' Add a field to the table. False if not added, or already added. '''
        if not ztype in TableDef.SupportedTypes:
            return False
        if name in self.fields:
            return False
        name = TableDef.Normalize(name)
        self.fields[name] = ztype
        return True

    def remove_field(self, name):
        ''' Remove a field from a table. Always returns True. '''
        if name in self.fields:
            self.fields.pop(name)
        return True

    def change_field(self, name, ztype):
        ''' Change the data-type for an existing field. '''
        if not ztype in TableDef.SupportedTypes:
            return False
        if name not in self.fields:
            return False
        self.fields[name] = ztype
        return True

    def __str__(self):
        ''' Program usable string. '''
        result = self._name + " {"
        bFirst = True
        for ref in self.fields:
            if not bFirst:
                result = result + ","
            result = result + ref + ':' + self.fields[ref]
            bFirst = False
        result = result + "}"
        return result

    def __repr__(self):
        ''' Factory usable string. '''
        result = str(type(self)) + ' : '
        result = result + str(self)
        return result

    @staticmethod
    def Normalize(name):
        ''' Create an SQL-friendly field name. '''
        name = name.strip()
        name = name.replace(' ', '_')
        return name


if __name__ == "__main__":
    ztable = TableDef()
    for key in TableDef.SupportedTypes:
        if ztable.add_field("z Customer " + key, key) is False:
            raise Exception("Error 001: " + str(type(ztable)))
    assert(ztable.get_table_name() == "Default")
    ztable.set_table_name("   nergal zoom tik \t ")
    assert(ztable.get_table_name() == "nergal_zoom_tik")
    print(repr(ztable))
    
