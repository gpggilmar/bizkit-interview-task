from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    filteredUsers = []
    unique_id = set()
    
    if not args:
        return USERS
 
    for key, value in args.items():
        if(key == 'id'):
            getFilteredUserByID(value, filteredUsers, unique_id)
            continue
        elif(key == 'name'):
            getFilteredUserByName(value, filteredUsers, unique_id)
            continue
        elif(key == 'age'):
            getFilteredUserByAge(value, filteredUsers, unique_id)
            continue
        elif(key == 'occupation'): 
            getFilteredUserByOccupation(value, filteredUsers, unique_id)
            continue

    return filteredUsers

def getFilteredUserByID(value, filteredUsers, unique_id):
    for user in USERS:
        if(user["id"] == value):
            appendUniqueObject(user, filteredUsers, unique_id)

def getFilteredUserByName(value, filteredUsers, unique_id):
    for user in USERS:
        if(value.lower() in user["name"].lower()):
            appendUniqueObject(user, filteredUsers, unique_id)

def getFilteredUserByAge(value, filteredUsers, unique_id):
    for user in USERS:
        if(abs(user["age"] - int(value)) <= 1):
            appendUniqueObject(user, filteredUsers, unique_id)

def getFilteredUserByOccupation(value, filteredUsers, unique_id):
    for user in USERS:
        if(value.lower() in user["occupation"].lower()):
            appendUniqueObject(user, filteredUsers, unique_id)

def appendUniqueObject(user, filteredUsers, unique_id):
    if(user["id"] not in unique_id):
        filteredUsers.append(user)
        unique_id.add(user["id"])

