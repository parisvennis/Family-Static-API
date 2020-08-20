
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
import uuid 

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {'first_name':'David','last_name':last_name,'id':0,'age':24,'lucky_numbers':[2,16]},
            {'first_name':'Paris','last_name':last_name,'id':1,'age':23,'lucky_numbers':[7,21]},
            {'first_name':'Tiger','last_name':last_name,'id':2,'age':32,'lucky_numbers':[11,44]}
            ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        # while member_id=
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)
        # fill this method and update the return
        return None


    def delete_member(self, id):
        # fill this method and update the return
        for position in range(len(self._members)):
            if self._members[position]["id"] == id:
                self._members.pop(position)
                return None
        

    def get_member(self, id):
        # fill this method and update the return
        for m in self._members:
            if m["id"] == int(id):
                return m

        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members