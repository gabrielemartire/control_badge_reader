
from db.seed import ROLES, USERS, BADGES, SECTORS, BADGE_READERS, WARNINGS, ACCESSES, BADGE_READERS_ROLES, BADGE_READERS_WARNINGS
from actions.crud_role import create_role
from actions.crud_user import create_user
from actions.crud_badge import create_badge
from actions.crud_sector import create_sector
from actions.crud_badge_reader import create_badge_reader
from actions.crud_warning import create_warning
from actions.crud_access import create_access
from actions.crud_badge_reader_role import create_badge_reader_role
from actions.crud_badge_reader_warning import create_badge_reader_warning


def use_seed(session):

    # SEED ROLES
    for r in ROLES:
        create_role(session = session, role_info = r)

    # SEED USERS
    for u in USERS:
        create_user(session = session, user_info = u)

    # SEED BADGES
    for b in BADGES:
        create_badge(session = session, badge_info = b)

    # SEED SECTORS
    for s in SECTORS:
        create_sector(session = session, sector_info = s)

    # SEED BADGE_READERS
    for br in BADGE_READERS:
        create_badge_reader(session = session, badge_reader_info = br)

    # SEED WARNINGS
    for w in WARNINGS:
        create_warning(session = session, warning_info = w)

    # SEED ACCESSES
    for a in ACCESSES:
        create_access(session = session, access_info = a)

    # SEED BADGE_READERS_ROLES (join table)
    for brr in BADGE_READERS_ROLES:
        create_badge_reader_role(session = session, badge_reader_role_info = brr)

    # SEED BADGE_READERS_WARNINGS (join table)
    for brw in BADGE_READERS_WARNINGS:
        create_badge_reader_warning(session = session, badge_reader_warning_info=brw)
