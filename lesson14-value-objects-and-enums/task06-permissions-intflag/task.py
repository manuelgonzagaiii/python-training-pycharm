"""Role Permissions with IntFlag

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from enum import IntFlag, auto


class Permission(IntFlag):
    NONE = 0
    READ = auto()
    WRITE = auto()
    REFUND = auto()
    MANAGE_USERS = auto()
    EXPORT = auto()

    # TODO: define class-level role constants, e.g.
    # CLERK = READ | WRITE  ;  ADMIN = everything
    def grants(self, needed: "Permission") -> bool:
        # TODO: return True if self contains all bits in `needed`
        ...

"""

# Your code here.
