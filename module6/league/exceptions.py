class DuplicateOid(Exception):
    def __init__(self, oid):
        super().__init__(f"Duplicate OID: {oid}")
        self.oid = oid


class DuplicateEmail(Exception):
    def __init__(self, email):
        super().__init__(f"Duplicate Email: {email}")
        self.email = email


