#!/usr/bin/env python3

import sys
import re
import os
import csv
import operator

#Abro dos diccionarios
errors = {} #que lleve la cuenta de los errores y el tipo de error
per_user = {} #que ordenos los usuarios y el numerod e mensajes divididos en INFO y en ERROR

with open("Curso 2\Log_Analysis_Final_project\syslog.log") as file:
    for log in file.readlines():
        match = re.search(r"ticky: ([\w]+) ([\w\s']*) ?(\[#\d*\])? \((.*)\)$", log)
        code, error_msg, ticket, user = match.group(1), match.group(2), match.group(3), match.group(4)
        #print("Usurio: {}, Codigo: {} Mensaje: {}".format(user, code, error_msg))
        #errors
        if error_msg not in errors.keys():
            if code == "ERROR":
                errors[error_msg] = 1
        else:
            errors[error_msg] += 1
        #per user
        if user not in per_user.keys():
            per_user[user] = {}
        if code == "ERROR":
            if "ERROR" not in per_user[user]:
                per_user[user]["ERROR"] = 1
            else:
                per_user[user]["ERROR"] += 1
        elif code == "INFO":
                if "INFO" not in per_user[user]:
                    per_user[user]["INFO"] = 1
                else:
                    per_user[user]["INFO"] += 1

file.close()           

#print(errors)
#print(per_user)

#let's sort the errors by the most common
sorted_errors = sorted(errors.items(), key = operator.itemgetter(1), reverse=True)
print(sorted_errors)
sorted_users = sorted(per_user.items(), key = operator.itemgetter(0))
print(sorted_users)

#Save thoses list in csv error_message.csv and user_statistics.csv.

with open("error_message.csv", "w") as error_message:
    writer = csv.writer(error_message)
    writer.writerows(sorted_errors)

with open("user_statistics.csv", "w", ) as user_statistics:
    writer = csv.writer(user_statistics)
    writer.writerows(sorted_users)