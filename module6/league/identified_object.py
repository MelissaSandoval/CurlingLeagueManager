from module6.league.exceptions import DuplicateOid, DuplicateEmail
class IdentifiedObject:
    """
    An abstract class...no instances of it will be created.
    """

    def oid(self):
        """[r/o prop] -- the object id for this object"""
        return self._oid

    def __init__(self, oid):
        """-- initialization method that sets the oid property
         as specified by the argument"""
        self._oid = oid

    def __eq__(self, other):
        """-- two IdentifiedObjects are equal if they have the
        same type and the same oid"""
        pass

    def __hash__(self):
        """-- return hash code based on object's oid"""
        return hash(self.oid)
