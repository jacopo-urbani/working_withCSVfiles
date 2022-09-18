# -*- coding: utf-8 -*-

import csv
import shutil
import os


def insert_person(person_file, first_name, last_name):
    # creating a copy of function file
    # using the file name that already exist and the destination directory

    copy_person_file = shutil.copy(person_file, dst=',')

    # opening the copy in reading mode and the original file in append mode
    with open(copy_person_file, 'r') as p1, open(person_file, 'a') as p2:

        # adding +1 to last index if the file is not empty

        last_line = p1.readlines()[-1]
        last_number = last_line.partition(',')[0]
        try:
            new_number = int(last_number) + 1
        except:
            # index=1 if the file is empty and updating it with the new record
            new_number = 1
            p2.writelines('Index,FirstName,LastName\n')

        # returning the index corresponding to the new person just inserted or None if no new record was added
        if first_name != '' and last_name != '':
            line = str(new_number) + ',' + first_name + ',' + last_name + '\n'
            p2.writelines(line)
            return new_number
        else:
            pass


def insert_colleague(person_file, colleagues_file, first_name, last_name, dept, place):
    # creating a copy of function file
    # using the file name that already exist and the destination directory
    copy_colleague_file = shutil.copy(colleagues_file, dst=',')
    with open(copy_colleague_file, 'r') as c1, open(colleagues_file, 'a') as c2:

        # adding +1 to last index if the file is not empty
        last_line = c1.readlines()[-1]
        last_number = last_line.partition(',')[0]
        try:
            new_number = int(last_number) + 1
        except:
            # index=1 if the file is empty and updating it with the new record
            new_number = 1
            c2.writelines('Index,Dept,Place\n')

        # returning the index corresponding to the new person just inserted or None if no new record (in the colleagues_file) was added
        if first_name != '' and last_name != '':
            insert_person(person_file, first_name, last_name)
            if dept != '' and place != '':
                line = str(new_number) + ',' + str(dept) + ',' + str(place) + '\n'
                c2.writelines(line)

                return new_number
            else:
                pass
        else:
            pass


def insert_friend(person_file, friends_file, first_name, last_name, street, city, country, phone):
    # creating a copy of function file
    # using the file name that already exist and the destination directory
    copy_friends_file = shutil.copy(friends_file, dst=',')
    with open(copy_friends_file, 'r') as f1, open(friends_file, 'a') as f2:

        # adding +1 to last index if the file is not empty
            last_line = f1.readlines()[-1]
            last_number = last_line.partition(',')[0]
            try:
                new_number = int(last_number) + 1

            # index=1 if the file is empty and updating it with the new record
            except:
                new_number = 1
                f2.writelines('Index,Street,City,Country,Phone\n')

        # returning the index corresponding to the new person just inserted or None if no new record (in friends_file) was added
            if first_name != '' and last_name != '':
                insert_person(person_file, first_name, last_name)
                if phone != '' and street != '' and city != '' and country != '':
                    line = str(new_number) + ',' + street + ',' + country + ',' + city + ',' + str(phone) + '\n'
                    f2.writelines(line)
                    return new_number
                else:
                    pass
            else:
                pass


def update_field(data_file, target, field_name, field_value):
    # checking if the file is consistent and create a variable with the last index
    if os.stat(data_file).st_size == 0:
        pass
    else:
        with open(data_file, 'r') as u1:
            last_line = u1.readlines()[-1]
            last_number = last_line.partition(',')[0]

        with open(data_file) as u1:

            # creating lists of csv rows,
            file_reader = csv.reader(u1, delimiter=',')

            # creating an empty list to store names of columns
            list_of_column_names = []

            # loop to iterate through the rows of csv
            for row in file_reader:
                # adding the first row
                list_of_column_names.append(row)

                # breaking the loop after the first iteration
                break
            # taking the first item in the list (which is a list itself)
            headers = list_of_column_names[0]

        # checking if the target and the field_name belong to the file
        if target > int(last_number) or field_name not in headers:
            pass
        else:
            with open(data_file, "r") as u1:
                file_dict_reader = csv.DictReader(u1)
                # creating an empty list which will contain all the updated rows
                updated_list = []
                # for any row in the file, checking if its index equals to the target
                for r in file_dict_reader:
                    if int(r[headers[0]]) == target:
                        # overwriting the row which are supposed to be updated
                        row = {**r, field_name: str(field_value)}
                        updated_list.append(row)
                    else:
                        # rewrite rows which are supposed not to change
                        row = {**r}
                        updated_list.append(row)

            # returning True if update was actually done
            with open(data_file, "w", newline='') as u1:
                data = csv.DictWriter(u1, delimiter=',', fieldnames=headers)
                # writing names of columns
                data.writerow(dict((heads, heads) for heads in headers))
                # writing rows
                data.writerows(updated_list)
            return True


def delete_person(data_file, target):
    if os.stat(data_file).st_size == 0:
        pass
    else:
        with open(data_file, 'r') as p2:
            last_line = p2.readlines()[-1]
            last_number = last_line.partition(',')[0]

    if target > int(last_number):
        pass
    else:
        # creating a copy of function's first parameter
        # using the file name that already exist in the destination directory
        copy_delete_file = shutil.copy(data_file, dst=',')
        with open(copy_delete_file, 'r') as d1, open(data_file, 'w') as d2:
            file_writer = csv.writer(d2)

            for row in csv.reader(d1):
                # writing all rows unless the one which has the index corresponding to the target
                if row[0] != str(target):
                    file_writer.writerow(row)
        copy2_delete_file = shutil.copy(data_file, dst=',')
        with open(copy2_delete_file, newline='') as d1, open(data_file, 'w', newline='') as d2:
            file_writer = csv.writer(d2)
            for row in csv.reader(d1):
                if row:
                    file_writer.writerow(row)
        return 'Successfully deleted'


'''
#Example:
print(insert_person('people.txt', 'jack', 'brown'))
print(insert_colleague('people.txt','colleagues.txt', 'jack', 'brown', 'marketing', 'Milan' ))
print(insert_friend('people.txt', 'friends.txt', 'jack', 'brown', 'Rome street 1','NY','US','33483'))
print(update_field('people.txt', 1, 'FirstName', 'david'))
print(delete_person('friends.txt', 1))
'''