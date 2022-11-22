import sys
import pandas as pd
def MakeDump(table):
    sys.stdin = open(f'{table}.txt','r', encoding='utf-8')
    user_num = int(input())
    input()
    users_list = []
    user_column = []
    for p in range(user_num+2):
        userInfo_line = input().split('|')
        userInfo_data = []
        for q in range(len(userInfo_line)):
            userInfo_line[q] = userInfo_line[q].strip()
            if userInfo_line[q]:
                userInfo_data.append(userInfo_line[q])
        
        if p == 0:
            user_column = userInfo_data[1:]
        elif p >= 2:
            users_list.append(userInfo_data[1:])
    # print(user_column, users_list)
    return user_column, users_list, table


def MakedatetimeDump(table):
    sys.stdin = open(f'{table}.txt','r', encoding='utf-8')
    user_num = int(input())
    input()
    users_list = []
    user_column = []
    created_datetime_pos = -1
    for p in range(user_num+2):
        userInfo_line = input().split('|')
        userInfo_data = []
        for q in range(len(userInfo_line)):
            userInfo_line[q] = userInfo_line[q].strip()
            if userInfo_line[q]:
                if q == created_datetime_pos:
                    userInfo_line[q] = userInfo_line[q] +'00'
                userInfo_data.append(userInfo_line[q])
        
        if p == 0:
            user_column = userInfo_data[1:]
            for q in range(len(userInfo_data)):
                if userInfo_data[q] == "created_datetime":
                    created_datetime_pos += q+2
        elif p >= 2:
            users_list.append(userInfo_data[1:])
    # print(user_column, users_list)
    return user_column, users_list, table


def MakeChallengeDump(table):
    sys.stdin = open(f'{table}.txt','r', encoding='utf-8')
    user_num = int(input())
    input()
    users_list = []
    user_column = []
    for p in range(user_num+2):
        userInfo_line = input().split('|')
        userInfo_data = []
        for q in range(len(userInfo_line)):
            userInfo_line[q] = userInfo_line[q].strip()
            if userInfo_line[q]:
                userInfo_data.append(userInfo_line[q])
        
        if p == 0:
            user_column = userInfo_data[1:]
        elif p >= 2:
            users_list.append(userInfo_data[1:])
    input()
    for p in range(user_num+2):
        userInfo_line = input().split('|')
        userInfo_data = []
        for q in range(len(userInfo_line)):
            userInfo_line[q] = userInfo_line[q].strip()
            if userInfo_line[q]:
                userInfo_data.append(userInfo_line[q])
        
        if p == 0:
            user_column = user_column + userInfo_data
        elif p >= 2:
            users_list[p-2] = users_list[p-2] + userInfo_data
    input()
    for p in range(user_num+2):
        userInfo_line = input().split('|')
        userInfo_data = []
        for q in range(len(userInfo_line)):
            userInfo_line[q] = userInfo_line[q].strip()
            if userInfo_line[q]:
                userInfo_data.append(userInfo_line[q])
        
        if p == 0:
            user_column = user_column + userInfo_data
        elif p >= 2:
            users_list[p-2] = users_list[p-2] + userInfo_data
    # print(user_column, users_list)
    return user_column, users_list
