from  insert_data import InsertData
from user import User
if __name__ == '__main__':


    # "C:/Users/הילה/Documents/אלישבע/google_project/2021-archive/RFC/1"
    insert_data=InsertData("C:/Users/הילה/Documents/אלישבע/google_project/2021-archive")
    insert_data.insert_data_to_DB()
    user=User().run()
