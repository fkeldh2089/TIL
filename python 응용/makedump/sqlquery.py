# INSERT INTO user (auth_code,login_type,nickname,profile_img,user_description, user_flag, user_score)
#  values (concat('authcode',i), '', concat('User',i), concat('Profileimg',i), concat('desc',i), 1, i*3);
import random
# import sys
# import pandas as pd
# sys.stdout = open('output.txt','w', encoding='utf-8')


# rct3 = pd.date_range(start='20221015', end='20221117')
# dt_list = rct3.strftime("%Y%m%d").to_list()


classification_type_sql = """-- classification type
INSERT INTO classification_type (classification_type_name) values('Drink water');
INSERT INTO classification_type (classification_type_name) values('Study');
INSERT INTO classification_type (classification_type_name) values('Exercise');
INSERT INTO classification_type (classification_type_name) values('Salad');"""

challenge_preset_sql = """-- challenge preset
INSERT INTO  challenge_preset (end_time,preset_description,start_time,step_count,preset_topic,classification_type_id,auth_type,preset_img)
values( '230000', 'wake up des', '010000', 0, '일어나서 물마시기', 1,'class', "no preset img");\n
INSERT INTO  challenge_preset (end_time,preset_description,start_time,step_count,preset_topic,classification_type_id,auth_type,preset_img)
values( '230000', 'study des', '010000', 0, '하루하루 공부해 나가기', 2,'class', "no preset img");\n
INSERT INTO  challenge_preset (end_time,preset_description,start_time,step_count,preset_topic,classification_type_id,auth_type,preset_img)
values( '230000', 'Exercise des', '010000', 0, '매일 운동하기', 3,'class', "no preset img");\n
INSERT INTO  challenge_preset (end_time,preset_description,start_time,step_count,preset_topic,auth_type,preset_img)
values( '230000', 'pills des', '010000', 0, '매일 약 먹기', 'feature', "no preset img");\n
INSERT INTO  challenge_preset (end_time,preset_description,start_time,step_count,preset_topic,classification_type_id,auth_type,preset_img)
values( '230000', 'Salad des', '010000', 0, '1일 1샐러드', 4,'class', "no preset img");\n
INSERT INTO  challenge_preset (end_time,preset_description,start_time,step_count,preset_topic,auth_type,preset_img)
values( '230000', 'cleaning des', '010000', 0, '정리정돈 하기', 'feature', "no preset img");"""

ranking_challenge_sql = """-- challenge_cg
INSERT INTO challenge (auth_type,challenge_description,challenge_img,challenge_name,challenge_score,challenge_topic,end_date,end_time,invite_code,penalty_content,people_cnt,reward_content,start_date,start_time,challenge_preset_id) 
values ('class', 'wake_up_des', 'no_img', 'wake_up', 80, '일어나서 물마시기', '20221215','230000','IVT_CD1','no_penalty', 5,'no_reward', '20221015', '010000',1);
INSERT INTO challenge (auth_type,challenge_description,challenge_img,challenge_name,challenge_score,challenge_topic,end_date,end_time,invite_code,penalty_content,people_cnt,reward_content,start_date,start_time,challenge_preset_id) 
values ('class', 'study_des', 'no_img', 'study', 60, '하루하루 공부해 나가기', '20221215','230000','IVT_CD2','no_penalty', 4,'no_reward', '20221015', '010000',2);
INSERT INTO challenge (auth_type,challenge_description,challenge_img,challenge_name,challenge_score,challenge_topic,end_date,end_time,invite_code,penalty_content,people_cnt,reward_content,start_date,start_time,challenge_preset_id) 
values ('class', 'Exercise_des', 'no_img', 'Exercise', 80, '매일 운동하기', '20221215','230000','IVT_CD3','no_penalty', 5,'no_reward', '20221015', '010000',3);
INSERT INTO challenge (auth_type,challenge_description,challenge_img,challenge_name,challenge_score,challenge_topic,end_date,end_time,invite_code,penalty_content,people_cnt,reward_content,start_date,start_time,challenge_preset_id) 
values ('feature', 'pills_des', 'no_img', 'pills', 80, '매일 약 먹기', '20221215','230000','IVT_CD4','no_penalty', 5,'no_reward', '20221015', '010000',4);
INSERT INTO challenge (auth_type,challenge_description,challenge_img,challenge_name,challenge_score,challenge_topic,end_date,end_time,invite_code,penalty_content,people_cnt,reward_content,start_date,start_time,challenge_preset_id) 
values ('class', 'Salad_des', 'no_img', 'Salad', 80, '1일 1샐러드', '20221215','230000','IVT_CD5','no_penalty', 5,'no_reward', '20221015', '010000',5);
INSERT INTO challenge (auth_type,challenge_description,challenge_img,challenge_name,challenge_score,challenge_topic,end_date,end_time,invite_code,penalty_content,people_cnt,reward_content,start_date,start_time,challenge_preset_id) 
values ('feature', 'cleaning_des', 'no_img', 'cleaning', 80, '정리정돈 하기', '20221215','230000','IVT_CD6','no_penalty', 5,'no_reward', '20221015', '010000',6);
-- user cg
INSERT INTO challenge (auth_type,challenge_description,challenge_img,challenge_name,challenge_score,challenge_topic,end_date,end_time,invite_code,penalty_content,people_cnt,reward_content,start_date,start_time) 
values ('no', 'not_jam', 'no_img', 'not_jam_at_12', 80, 'what_is_topic', '20221215','170000','IVT_CD6','no_penalty', 5,'no_reward', '20221015', '130000');"""

classification_keyword_sql = """INSERT INTO classification_keyword (keyword, classification_type_id) values ('cup', 1);
INSERT INTO classification_keyword (keyword, classification_type_id) values ('water', 1);
INSERT INTO classification_keyword (keyword, classification_type_id) values ('book', 2);
INSERT INTO classification_keyword (keyword, classification_type_id) values ('laptop', 2);
INSERT INTO classification_keyword (keyword, classification_type_id) values ('machine', 3);
INSERT INTO classification_keyword (keyword, classification_type_id) values ('active', 3);
INSERT INTO classification_keyword (keyword, classification_type_id) values ('salad', 4);
INSERT INTO classification_keyword (keyword, classification_type_id) values ('fruit', 4);"""

auth_classification_sql = """INSERT INTO auth_classification (challenge_id, classification_type_id) values (1, 1);
INSERT INTO auth_classification (challenge_id, classification_type_id) values (2, 2);
INSERT INTO auth_classification (challenge_id, classification_type_id) values (3, 3);
INSERT INTO auth_classification (challenge_id, classification_type_id) values (5, 4);"""



def createQuery(to_table:str, cols: list, vals: list):

    start_query = 'INSERT INTO '+ to_table + ' (`' + '`, `'.join(cols) + "`)"
    for val in vals:
        val_qurery = "("
        for val_item in val:
            if type(val_item) is str:
                val_qurery += "'"+val_item+"', "
            else:
                val_qurery += str(val_item)+", "
        val_qurery = val_qurery[:-2]+");"
        query = start_query + "VALUES "+val_qurery
        print(query)

# ['1111','kakao','nickname','profile_img','user_description', 'user_flag', 'user_score']
def createvals(names: list):
    vals = []
    user_descriptions = ["안녕하세요, 좋은 하루되세요", "아자아자 화이팅!", "오늘도 열심히 달려봅시다"]
    for name in names:
        val = []
        val.append('1111')  # auth_code
        val.append('kakao')  # login_type
        val.append(name)  # nickname
        val.append('profile_img')  # profile_img
        val.append(random.choice(user_descriptions))  # user_description
        val.append(0)  # profile_img
        val.append(random.randint(1, 90))  # user_score
        vals.append(val)
    # print(vals)
    return vals



# cols1 = ['auth_code','login_type','nickname','profile_img','user_description', 'user_flag', 'user_score']
# names = ["홍제민", "우시은", "원찬호", "김현영", "조혜림", "이", "도", "경", "김희성", "안희경", "배은경", "김무종", "박세현", "홍성영", "김주한", "지우", "슈뢰딩거"]
# vals1 = createvals(names)
# cols2 = ['challenge_id', 'user_id']
# vals2 = [[random.randint(1, 7), i+1] for i in range(len(names))]
# cols3 = ['created_datetime','feed_content','feed_img','feed_type','participation_id']

# feed_contents = ["오늘도 해냈다.", "이래가지고 언제 끝나냐,,", "아니 이게 무슨일이람,", "오늘도 간신히 넘어가는구나", "참 쉬웠어요"]
# print("use ollenge;")
# createQuery('user', cols1, vals1)
# print(classification_type_sql)
# print(challenge_preset_sql)
# print(ranking_challenge_sql)
# createQuery('participation', cols2, vals2)
# print(classification_keyword_sql)
# print(auth_classification_sql)
# for i in range(len(names)):
#     vals3 = []
#     for dt in dt_list:
#         val3 = [int(dt), random.choice(feed_contents), 'feed_img', 1, i+1]
#         vals3.append(val3)
#     createQuery('feed', cols3, vals3)


# # badge logic

# badge_type_list = ["WakeUp", "Study", "Exercise", "Pills", "Salad", "Cleaning", "User"]
# for i in range(len(names)):
#     cols4 = ["badge_flag", "created_datetime", "grade", "type", "challenge_preset_id", "user_id"]
#     for j in range(len(badge_type_list)):
#         if j >= 6:
#             cols4 = ["badge_flag", "created_datetime", "grade", "type", "user_id"]
#         badge_type = badge_type_list[j]
#         badge_grade = random.randint(0, 4)
#         vals4 = []
#         if badge_grade == 0:
#             continue
#         else:
#             badge_flag_list = [0]*badge_grade
#             for p in range(badge_grade):
#                 badge_flag_list[p] = random.randint(0, 1)
#             for p in range(badge_grade):
#                 if badge_flag_list[p]:
#                     badge_flag_list[p] = True
#                 else:
#                     badge_flag_list[p] = False
#             created_datetime_list = random.sample(dt_list, badge_grade)
#             created_datetime_list.sort()
#             for p in range(badge_grade):
#                 if j >=6:
#                     val4 = [badge_flag_list[p], int(created_datetime_list[p]), p+1, badge_type, i+1]
#                 else:
#                     val4 = [badge_flag_list[p], int(created_datetime_list[p]), p+1, badge_type, j+1, i+1]
#                 vals4.append(val4)
#             createQuery('badge', cols4, vals4)


# for i in range(len(names)):
#     print(f"UPDATE user SET selected_badge_id = (SELECT badge_id FROM badge WHERE badge.user_id=user.user_id LIMIT 1) WHERE user.user_id={i+1};")
