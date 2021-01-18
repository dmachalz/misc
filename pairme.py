# This script of used for creating pairings for chat dates for molecular design lab members.
# Replace user1... userN with real user names before usage.
# @author davidm
import itertools
import csv
import copy
import random

# Variables
# List of people to be paired
userlist = ['user1', 'user2', 'user3', 'user4', 'user5']
# Number of weeks to do the user pairing for.
n_weeks = 4
# Define the path to the outputfile in CSV format.
outcsv = '~/pairtable.csv'

# Creating a pool of all possible user combinations. Format is list of tuples.
combis = [x for x in itertools.combinations(userlist, 2)]

# Initiate pairings dictionary
pairingsdict = {}

for week in range(n_weeks):
    week += 1

    # Creating deep copy of user list to eliminate users in the process
    remaining_users = copy.deepcopy(userlist)
    pairings = []

    #for pair in combis:
    #    user1, user2 = pair[0], pair[1]
    if (len(userlist) % 2) == 0:
        while len(remaining_users) > 0:
            pair = random.choice(combis)
            user1, user2 = pair[0], pair[1]
            if (user1 in remaining_users) and (user2 in remaining_users):
                pairings.append(pair)
                remaining_users.remove(user1)
                remaining_users.remove(user2)
        print(pairings)


    elif (len(userlist) % 2) != 0 and len(userlist) > 0:
        while len(remaining_users) > 1:
            pair = random.choice(combis)
            user1, user2 = pair[0], pair[1]
            if (user1 in remaining_users) and (user2 in remaining_users):
                pairings.append([user1, user2])
                remaining_users.remove(user1)
                remaining_users.remove(user2)
        # add user to random group
        else:
            last_user = remaining_users[0]
            happy2 = random.choice(pairings)
            happy2 = happy2.append(last_user)
        print(pairings)

    else:
        if len(userlist) == 0 or len(userlist) is None:
            print('Please specify the list of users to be paired as the variable "userlist" in the script.')

# Writing out the results.


with open(outcsv, 'w') as f:
    csv_out=csv.writer(f)
    f.write('+++\n')
    csv_out.writerows(pairings)
    f.write('+++\n')
f.close()
