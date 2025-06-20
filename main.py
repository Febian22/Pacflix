class User:
    database = {'Services': ['Stream','Download','SD Quality','HD Quality', 'UHD Quality', 'Num of Devices','Content','Price'],
            'Basic Plan':[1,1,1,0,0,1,'3rd Party Movie Only',120], 
           'Standard Plan': [1,1,1,1,0,2,'Basic Plan Content + Sports(F1, Football, Basketball)',160],
           'Premium Plan': [1,1,1,1,1,4,'Basic Plan + Standard Plan + PacFlix Original Series/Movie',200]
           }
    
    def __init__(_, username):
        _.username = username

    def check_benefit(_):
        '''
        Show all benefit plan

        parameter:
        None
        return:
        None
        '''
        print("PacFlix all Plan Benefit : \n")
        header = "|"
        content_list = []
        for component in _.database:
            length_counter = max([len(str(x)) for x in _.database[component]]) + 10
            header += component.center(length_counter)
            header += "|"
            if component == 'Services':
                for index in range(len(_.database[component])):
                    content = "|"
                    content += _.database[component][index].center(length_counter)
                    content += "|"
                    content_list.append(content)
            else:
                for index in range(len(_.database[component])):
                    content = ""
                    if index < 5:
                        if _.database[component][index] == 1:
                            content = "V"
                        else:
                            content = "X"
                    elif index == 5:
                        content = str(_.database[component][index])
                    elif index == 6:
                        content = _.database[component][index]
                    elif index == 7:
                        content = f"Rp. {_.database[component][index]*1000}"
                        
                    content = content.center(length_counter)
                    content += "|"
                    content_list[index] += content
        print(header)
        for content in content_list:
            print(content)
        print("\n"*2)


class NewUser(User):
    def __init__(_, name):
        User.__init__(_, name)
    
    def pick_plan(_, new_plan:str, referral_code:str):
        '''
        method pick_plan
        parameter :
        new_plan (str) has to be 1 out of 3 plan : Basic Plan, Standard Plan, Premium Plan
        referral_code (str) can be blanked ''

        return:
        None

        Print: 
        " You choose : {new_plan} for Rp. {price} "
        '''
        _.existing_referral = ['PacflixSuper',
                               'PacflixMantap',
                               'PacflixJuara',
                               'bagus-9f92'
                               ]
        if new_plan not in _.database:
            raise TypeError("Choose 1 out of 3 plan: Basic Plan, Standard Plan, Premium Plan")
        if referral_code in _.existing_referral:
            price = _.database[new_plan][7] * 1000 * (1-0.04)
        else:
            print("Refferal Code Doesn't Exist")
            price = _.database[new_plan][7] * 1000
        
        print(f"You choose : {new_plan} for Rp. {price} \n")


class ExistUser(User):
    def __init__(_, name, plan:str, duration:int):
        User.__init__(_, name)
        if plan not in _.database:
            raise TypeError("Choose 1 out of 3 plan: Basic Plan, Standard Plan, Premium Plan")
        _.plan = plan
        _.duration = duration
    
    def check_plan(_):
        '''
        method check_plan
        parameter :
        None

        return:
        None

        Print: 
        Benefit Table of current plan
        '''
        print(f"Username : {_.username}")
        print(f"Plan Choosed : {_.plan}")
        print(f"Duration on plan : {_.duration}\n")
        header = '|'
        content_list = []
        for component in ['Services', _.plan]:
            length_counter = max([len(str(x)) for x in _.database[component]]) + 10
            header += component.center(length_counter)
            header += "|"
            if component == 'Services':
                for index in range(len(_.database[component])):
                    content = "|"
                    content += _.database[component][index].center(length_counter)
                    content += "|"
                    content_list.append(content)
            else:
                for index in range(len(_.database[component])):
                    content = ""
                    if index < 5:
                        if _.database[component][index] == 1:
                            content = "V"
                        else:
                            content = "X"
                    elif index == 5:
                        content = str(_.database[component][index])
                    elif index == 6:
                        content = _.database[component][index]
                    elif index == 7:
                        content = f"Rp. {_.database[component][index]*1000}"
                        
                    content = content.center(length_counter)
                    content += "|"
                    content_list[index] += content
        print(header)
        for content in content_list:
            print(content)
        print("\n"*2)

    def upgrade_plan(_, new_plan):
        '''
        method upgrade_plan
        parameter :
        new_plan (str) has to be 1 out of 3 plan : Basic Plan, Standard Plan, Premium Plan
        The new plan can only upgrade the current not downgrade

        return:
        None

        Print: 
        " You choose to upgrade to : {new_plan} for Rp. {price} "
        '''
        key_database = list(_.database.keys())
        if new_plan not in _.database:
            raise TypeError("New plan is not Existed")
        new_index = key_database.index(new_plan)
        old_index = key_database.index(_.plan)

        if old_index >= new_index:
            print('You can only upgrade to higher tier')
        elif old_index > 2:
            print("You cant upgrade anymore")
        else:
            discount = 0
            if _.duration > 12:
                discount += 0.05
            price = _.database[new_plan][7] * 1000 * (1-discount)
            print (f"Upgrade {_.username}'s plan, from '{_.plan}' to '{new_plan}' for Rp. {int(price)}\n")





    
