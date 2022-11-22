from make_user import MakeDump, MakeChallengeDump, MakedatetimeDump
from sqlquery import createQuery
import pandas as pd
import sys
import random
import pandas as pd

rct3 = pd.date_range(start='20220101', end='20221117')
dt_list = rct3.strftime("%Y%m%d").to_list()
sys.stdout = open('output.txt','w', encoding='utf-8')


def createQuery(to_table:str, cols: list, vals: list):

    start_query = 'INSERT INTO '+ to_table + ' (`' + '`, `'.join(cols) + "`) "
    for val in vals:
        val_qurery = "("
        for val_item in val:
            if type(val_item) is str and val_item != "Null" and val_item != "True" and val_item != "False":
                val_qurery += "'"+val_item+"', "
            else:
                val_qurery += str(val_item)+", "
        val_qurery = val_qurery[:-2]+");"
        query = start_query + "VALUES "+val_qurery
        print(query)

print("use ollenge;")
users_column, users_data, user_table_name = MakeDump("user")
createQuery(user_table_name, users_column, users_data)
column, data, tablename = MakeDump("classification_type")
createQuery(tablename, column, data)
column, data, tablename = MakeDump("classification_keyword")
createQuery(tablename, column, data)
column, data, tablename = MakeDump("challenge_preset")
createQuery(tablename, column, data)
column, data = MakeChallengeDump("rank_challenge_current")
createQuery('challenge', column, data)
column, data = MakeChallengeDump("user_challenge_current")
createQuery('challenge', column, data)
column, data = MakeChallengeDump("rank_challenge_past")
createQuery('challenge', column, data)
column, data = MakeChallengeDump("user_challenge_past")
createQuery('challenge', column, data)
column, data = MakeChallengeDump("rank_challenge_future")
createQuery('challenge', column, data)
users_column, users_data, user_table_name = MakeDump("participation")
createQuery(user_table_name, users_column, users_data)
users_column, users_data, user_table_name = MakedatetimeDump("feed")
createQuery(user_table_name, users_column, users_data)
users_column, users_data, user_table_name = MakeDump("badge")
createQuery(user_table_name, users_column, users_data)

#
badge_type_list = ["ranking1", "ranking2", "ranking3", "ranking4", "ranking5", "ranking6","user"]
for i in range(1, 24):
    cols4 = ["badge_flag", "created_datetime", "grade", "type", "challenge_preset_id", "user_id"]
    for j in range(len(badge_type_list)):
        if j >= 6:
            cols4 = ["badge_flag", "created_datetime", "grade", "type", "user_id"]
        badge_type = badge_type_list[j]
        badge_grade = random.randint(0, 4)
        vals4 = []
        if badge_grade == 0:
            continue
        else:
            badge_flag_list = [0]*badge_grade
            for p in range(badge_grade):
                badge_flag_list[p] = random.randint(0, 1)
            for p in range(badge_grade):
                if badge_flag_list[p]:
                    badge_flag_list[p] = True
                else:
                    badge_flag_list[p] = False
            created_datetime_list = random.sample(dt_list, badge_grade)
            created_datetime_list.sort()
            for p in range(badge_grade):
                if j >=6:
                    val4 = [badge_flag_list[p], int(created_datetime_list[p]), p+1, badge_type, i+1]
                else:
                    val4 = [badge_flag_list[p], int(created_datetime_list[p]), p+1, badge_type, j+1, i+1]
                vals4.append(val4)
            createQuery('badge', cols4, vals4)


for i in range(1, 24):
    print(f"UPDATE user SET selected_badge_id = (SELECT badge_id FROM badge WHERE badge.user_id=user.user_id LIMIT 1) WHERE user.user_id={i+1};")


# additional challenge related 1's challenge
column, data = MakeChallengeDump("additional_challenge")
createQuery('challenge', column, data)

# create result
users_column, challenge_result_data, user_table_name = MakeDump("challenge_result")
result_len = len(challenge_result_data)
createQuery(user_table_name, users_column, challenge_result_data)

# update result id
chs = [25, 31, 32, 33, 34]
for i in range(result_len):
    TOCNT, UID = challenge_result_data[i]
    print(f"UPDATE challenge SET challenge_result_id = {i+1} WHERE challenge.challenge_id={chs[i]};")


users_column, users_data, user_table_name = MakeDump("auth_classification")
createQuery(user_table_name, users_column, users_data)