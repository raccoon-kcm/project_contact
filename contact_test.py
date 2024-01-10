# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 17:26:41 2022

@author: A
"""
import os.path

class Contact:
    contact_file_name = "contact_db.txt"
    contact_recycle_bin_file_name = "contact_recycle_bin_db.txt"
    contact_bookmark_file_name = "contact_bookmark_db.txt"
    items = ['name', 'phone_number', 'e_mail', 'addr', 'group', 'nickname']
    
    # 기존 클래스에서 group과 nickname 클래스 속성 추가 
    # def __init__(self, name = "", phone_number = "", e_mail = "", addr = "", group = "", nickname = ""):
    #     self.name = name
    #     self.phone_number = phone_number
    #     self.e_mail = e_mail
    #     self.addr = addr
    #     self.group = group
    #     self.nickname = nickname

    def __init__(self, name = "", phone_number = "", e_mail = "", addr = "", group = "", nickname = ""):
        self.__name = name
        self.__phone_number = phone_number
        self.__e_mail = e_mail
        self.__addr = addr
        self.__group = group
        self.__nickname = nickname        

    # 추가된 속성도 print 추가 하였음
    def print_info(self):
        print("Name: ", self.__name)
        print("Phone Number: ", self.__phone_number)
        print("E-mail: ", self.__e_mail)
        print("Address: ", self.__addr)
        print("Group: ", self.__group)
        print("Nickname: ", self.__nickname)
        print("")
    
    # getter 추가하였음
    # setter는 하지 않았는데 set함수로 한 번에 입력하기 때문에 꼭 필요하다고 생각되지 않아 넣지 않았
    @property #getter
    def name (self):
        return self.__name

    @property #getter
    def phone_number (self):
        return self.__phone_number

    @property #getter
    def e_mail (self):
        return self.__e_mail
    
    @property #getter
    def addr (self):
        return self.__addr
    
    @property #getter
    def group (self):
        return self.__group
    
    @property #getter
    def nickname (self):
        return self.__nickname
    
# 이름이 공백인지 아닌지 판단하는 함수, 공백이면 전화번호를 이름으로 대신 입력 
def check_name_blank(name, phone_number):

    if name == "" :
        return "".join(phone_number.split("-"))
    else:
        return name
# 핸드폰 번호가 중복이될 수 없고 빈칸이 될 수 없음
def pk_phone_number(contact_list):
    count = 0
    while 1:
        phone_number_str = input("Phone Number: ")
        
        for i in range(len(contact_list)):
            if phone_number_str == contact_list[i].phone_number: # 번호가 중복인지 판단
                print("중복된 전화번호 입니다.")
                print("다시 입력해 주세요.")
                count = 1
                break
            elif phone_number_str == "":                        # 번호가 공백인지 판단
                print("핸드폰 번호는 반드시 기재해야합니다.")
                print("다시 입력해 주세요.")
                count = 1
                break
            else:
                count = 0
        if count == 0:
            break
    return phone_number_str

# contact 입력 함수
def set_contact(contact_list):
    name = input("Name: ")
    phone_number = pk_phone_number(contact_list)
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    group = input("Group: ")
    nickname = input("Nickname: ")
    name = check_name_blank(name, phone_number)
    
    contact = Contact(name, phone_number, e_mail, addr, group, nickname)

    print("입력이 완료 되었습니다.")
    return contact

# enumerate 함수를 이용하여 연락처 출력 시 인덱스로 사용할 번호를 출력되게 하였음 
# contact 출력 함수
def print_contact(contact_list):
    print("")
    if (len(contact_list) == 0):
        print("출력할 연락처가 없습니다.")
    else:
        for i, contact in enumerate(contact_list):
            print("%d." % i)
            contact.print_info()

# 다양한 조건 검색, 수정, 삭제 함수에 사용됨 
# contact 검색 함수
def search_contact(contact_list):
    while 1:
        print_selection()
        search_items = [str(i + 1) for i in range(len(Contact.items))]
        num_search = input("검색할 항목 번호 입력:")
        
        if num_search in search_items:
            num_search = int(num_search)
            break
        else:
            print("다시 입력해주세요.\n")
    
    dummy_contact = []
    dummy_contact_index = []
    
    # 선택한 항목에 따라 검색결과를 어떤 항목으로 정렬할지 정하는 if절
    if num_search == 1:
        search_string = input("Name: ")
        print("\n")
        for i in range(len(contact_list)):
            if contact_list[i].name.find(search_string) >= 0:
                dummy_contact.append(contact_list[i])
                dummy_contact_index.append(i)       
        
        # 정렬 함수 실행
        # dummy_contact = sort_contact(dummy_contact, num_search)
        # print_contact(dummy_contact)
        # print_contact(sort_contact(dummy_contact, num_search))
        
    elif num_search == 2:
        search_string = input("Phone Number: ")
        print("\n")
        for i in range(len(contact_list)):
            if contact_list[i].phone_number.find(search_string) >= 0:   # in을 써도 되지만 find로 해보았음
                dummy_contact.append(contact_list[i])
                dummy_contact_index.append(i)        
        
        # 정렬 함수 실행
        # dummy_contact = sort_contact(dummy_contact, num_search)
        # print_contact(dummy_contact)
        # print_contact(sort_contact(dummy_contact, num_search))     
        
    elif num_search == 3:
        search_string = input("E-mail: ")
        print("\n")
        for i in range(len(contact_list)):
            if contact_list[i].e_mail.find(search_string) >= 0:
                dummy_contact.append(contact_list[i])
                dummy_contact_index.append(i)
                
        # 정렬 함수 실행
        # dummy_contact = sort_contact(dummy_contact, num_search)
        # print_contact(dummy_contact)
        # print_contact(sort_contact(dummy_contact, num_search))       
        
    elif num_search == 4:
        search_string = input("Address: ")
        print("\n")
        for i in range(len(contact_list)):
            if contact_list[i].addr.find(search_string) >= 0:
                dummy_contact.append(contact_list[i])
                dummy_contact_index.append(i)
                
        # 정렬 함수 실행
        # dummy_contact = sort_contact(dummy_contact, num_search)
        # print_contact(dummy_contact)
        # print_contact(sort_contact(dummy_contact, num_search))
    
    elif num_search == 5:
        search_string = input("Group: ")
        print("\n")
        for i in range(len(contact_list)):
            if contact_list[i].group.find(search_string) >= 0:
                dummy_contact.append(contact_list[i])
                dummy_contact_index.append(i)
                
        # 정렬 함수 실행
        # dummy_contact = sort_contact(dummy_contact, num_search)
        # print_contact(dummy_contact)
        # print_contact(sort_contact(dummy_contact, num_search))

    elif num_search == 6:
        search_string = input("Nickname: ")
        print("\n")
        for i in range(len(contact_list)):
            if contact_list[i].nickname.find(search_string) >= 0:
                dummy_contact.append(contact_list[i])
                dummy_contact_index.append(i)
        
        # 정렬 함수 실행
        # dummy_contact = sort_contact(dummy_contact, num_search)
        # print_contact(dummy_contact)
        # print_contact(sort_contact(dummy_contact, num_search))
    
    return (dummy_contact, dummy_contact_index, num_search)       # 다양한 함수에서 활용하기 위해 반환값이 존재함

# contact 수정 함수
def update_contact(contact_list):   
    (search_contact_list, index_contact, num_sort) = search_contact(contact_list)
    
    num_search_contact = len(search_contact_list)
    
    search_items = [str(i) for i in range(num_search_contact)]
    search_items.append('-1')
    
    # 해당 연락처를 찾지 못한 경우 
    if num_search_contact == 0:
        print("연락처를 찾지 못했습니다.")
    else:
        print_contact(search_contact_list)
        while 1:
            num_select_contact = input("수정할 연락처 번호 입력(종료 = -1):")
            
            if num_select_contact in search_items:
                num_select_contact = int(num_select_contact)
                break
            else:
                print_contact(search_contact_list)
                print("=" * 15)
                print("다시 입력해주세요.")
            
            # try:
            #     num_select_contact = int(input("수정할 연락처 번호 입력(종료 = -1):"))
            # except ValueError as e:
            #     print(e)
            #     print("다시 입력해주세요.\n")
            #     print_contact(search_contact_list)
            # else:
            #     break
            # finally:
            #     print("")
        
        if num_select_contact >= 0:
            # 
            contact_list[index_contact[num_select_contact]] = set_contact(contact_list)
            print("수정이 완료 되었습니다.")
        
        else:
            print("메인 화면으로 이동합니다.")

# contact 삭제 함수
def delete_contact(contact_list, recycle_bin_list, bookmark_list):
    # search 함수를 이용하여 제거할 연락처를 찾음
    (dummy_contact_list, index_contact, num_sort)= search_contact(contact_list)
    
    num_search_contact = len(dummy_contact_list)
    
    search_items = [str(i) for i in range(num_search_contact)]
    search_items.append('-1')
    
    print_contact(dummy_contact_list)
    
    if num_search_contact == 0:
        print("연락처를 찾지 못했습니다.")
    else:
        # 검색 결과 연락처가 여러 개 있는 경우도 포함
        while 1:
            num_select_contact = input("삭제할 연락처 번호 입력(종료 = -1):")
                
            if num_select_contact in search_items:
                num_select_contact = int(num_select_contact)
                break
            else:
                print("다시 입력해주세요.")

        if num_select_contact >= 0:
            # 휴지통 기능
            recycle_bin_list.append(contact_list[index_contact[num_select_contact]])
            # contact_list에 저장하던 즐겨찾기 정보가 사라지면 즐겨찾기의 정보도 삭제
            delete_contact_phone_number = contact_list[index_contact[num_select_contact]].phone_number
            del contact_list[index_contact[num_select_contact]]
            
            for i in range(len(bookmark_list)):
               if bookmark_list[i].phone_number == delete_contact_phone_number:
                   del bookmark_list[i]
                   break
            
            print("삭제가 완료 되었습니다.")
        else:
            print("메인 화면으로 이동합니다.")  

# 휴지통 기능을 하는 recycle_bin_list 추가, 즐겨찾기 기능을 하는 bookmark_list 추가
# 연락처 로드 함수
def load_contact(contact_list, recycle_bin_list, bookmark_list):
    file_dir_check = os.path.isfile(Contact.contact_file_name)
    
    if file_dir_check == True:
        with open (file = Contact.contact_file_name, mode = "rt", encoding = 'utf-8') as f:
            lines = f.readlines()
        
            items_num = len(Contact.items)
            num = len(lines) / items_num
            num = int(num)
        
            for i in range(num):
                name = lines[items_num*i].rstrip('\n')
                phone = lines[items_num*i+1].rstrip('\n')
                email = lines[items_num*i+2].rstrip('\n')
                addr = lines[items_num*i+3].rstrip('\n')
                group = lines[items_num*i+4].rstrip('\n')
                nickname = lines[items_num*i+5].rstrip('\n')
                
                contact = Contact(name, phone, email, addr, group, nickname)
                contact_list.append(contact)
    
    file_dir_check = os.path.isfile(Contact.contact_recycle_bin_file_name)
    
    if file_dir_check == True:
        with open (file = Contact.contact_recycle_bin_file_name, mode = "rt", encoding = 'utf-8') as f:
            lines = f.readlines()
        
            items_num = len(Contact.items)
            num = len(lines) / items_num
            num = int(num)
        
            for i in range(num):
                name = lines[items_num*i].rstrip('\n')
                phone = lines[items_num*i+1].rstrip('\n')
                email = lines[items_num*i+2].rstrip('\n')
                addr = lines[items_num*i+3].rstrip('\n')
                group = lines[items_num*i+4].rstrip('\n')
                nickname = lines[items_num*i+5].rstrip('\n')
                
                contact = Contact(name, phone, email, addr, group, nickname)
                recycle_bin_list.append(contact)

    file_dir_check = os.path.isfile(Contact.contact_bookmark_file_name)
    
    if file_dir_check == True:
        with open (file = Contact.contact_bookmark_file_name, mode = "rt", encoding = 'utf-8') as f:
            lines = f.readlines()
        
            items_num = len(Contact.items)
            num = len(lines) / items_num
            num = int(num)
        
            for i in range(num):
                name = lines[items_num*i].rstrip('\n')
                phone = lines[items_num*i+1].rstrip('\n')
                email = lines[items_num*i+2].rstrip('\n')
                addr = lines[items_num*i+3].rstrip('\n')
                group = lines[items_num*i+4].rstrip('\n')
                nickname = lines[items_num*i+5].rstrip('\n')
                
                contact = Contact(name, phone, email, addr, group, nickname)
                bookmark_list.append(contact)

# 휴지통 기능을 하는 recycle_bin_list 추가, 즐겨찾기 기능을 하는 bookmark_list 추가
# 연락처 저장 함수
def store_contact(contact_list, recycle_bin_list, bookmark_list):
    with open(file = Contact.contact_file_name, mode = "wt", encoding = 'utf-8') as f:
        for contact in contact_list:
            f.write(contact.name + '\n')
            f.write(contact.phone_number + '\n')
            f.write(contact.e_mail + '\n')
            f.write(contact.addr + '\n')
            f.write(contact.group + '\n')
            f.write(contact.nickname + '\n')
            
    with open(file = Contact.contact_recycle_bin_file_name, mode = "wt", encoding = 'utf-8') as f:
        for recycle_bin in recycle_bin_list:
            f.write(recycle_bin.name + '\n')
            f.write(recycle_bin.phone_number + '\n')
            f.write(recycle_bin.e_mail + '\n')
            f.write(recycle_bin.addr + '\n')
            f.write(recycle_bin.group + '\n')
            f.write(recycle_bin.nickname + '\n')
    
    with open(file = Contact.contact_bookmark_file_name, mode = "wt", encoding = 'utf-8') as f:
        for bookmark_list in bookmark_list:
            f.write(bookmark_list.name + '\n')
            f.write(bookmark_list.phone_number + '\n')
            f.write(bookmark_list.e_mail + '\n')
            f.write(bookmark_list.addr + '\n')
            f.write(bookmark_list.group + '\n')
            f.write(bookmark_list.nickname + '\n') 

# 즐겨찾기 함수
def bookmark_contact(contact_list, bookmark_list):    
    bookmark_items = [str(i + 1) for i in range(4)]
    
    while 1:
        str_bookmark = ""        
        
        print("1. 즐겨찾기 출력")
        print("2. 즐겨찾기 추가")
        print("3. 즐겨찾기 제거")
        print("4. 메인화면 가기")
        str_bookmark = input("메뉴선택: ")
        if str_bookmark in bookmark_items:
            num_bookmark = int(str_bookmark)
            if num_bookmark == 1:
                print_contact(bookmark_list)
            elif num_bookmark == 2:
                # 리스트 검색
                (search_contact_list, index_contact, num_sort) = search_contact(contact_list)
                # 연락처 선택
                num_search_contact = len(search_contact_list)
            
                print_contact(search_contact_list)
                
                search_items = [str(i) for i in range(num_search_contact)]
                search_items.append('-1')
                
                if num_search_contact == 0:
                    print("연락처를 찾지 못했습니다.")
                else:
                    # print_contact(search_contact_list)
                    while 1:
                        count = 0
                        num_select_contact = input("즐겨찾기 추가할 연락처 번호 입력(종료 = -1):")
                        
                        if num_select_contact in search_items:
                            num_select_contact = int(num_select_contact)
                            if num_select_contact >= 0:
                                for i in range(len(bookmark_list)):
                                    if bookmark_list[i].phone_number == contact_list[index_contact[num_select_contact]].phone_number:
                                        count = 1
                                        break
                                if count == 0:
                                    bookmark_list.append(contact_list[index_contact[num_select_contact]])
                                    print("즐겨찾기 추가가 완료 되었습니다.")
                                    break
                                else:
                                    print_contact(search_contact_list)
                                    print("중복된 즐겨찾기 연락처입니다.")
                                    print("다시 입력해주세요.")
                                
                            else:
                                print("이전 화면으로 이동합니다.")
                                break
                        else:
                            print_contact(search_contact_list)
                            print("=" * 15)
                            print("다시 입력해주세요.")
                            

            elif num_bookmark == 3:
                print_contact(bookmark_list)
                
                num_delete_bookmark = len(bookmark_list)
                
                if num_delete_bookmark == 0:
                    break
                
                else:
                    delete_bookmark_items = [str(i) for i in range(num_delete_bookmark)]
                    delete_bookmark_items.append('-1')
                    
                    while 1:
                        select_bookmark = input("북마크 제거할 연락처 번호 입력(종료 = -1):")
                        
                        if select_bookmark in delete_bookmark_items:
                            select_bookmark = int(select_bookmark)
                            break
                        else:
                            print_contact(bookmark_list)
                            print("=" * 15)
                            print("다시 입력해주세요.")
                    
                    if select_bookmark >= 0:
                        del bookmark_list[select_bookmark]
                        print("즐겨찾기 제거가 완료 되었습니다.")
                    else:
                        print("메인 화면으로 이동합니다.")
                
            elif num_bookmark == 4:
                break
        else:
            print("=" * 10)
            print("다시 입력해주세요.")
    

# 휴지통 기능 -> 연락처 복원과 휴지통 비우기만 구현하였음
# 휴지통 함수
def recycle_bin(contact_list, recycle_bin_list):
    recycle_items = [str(i + 1) for i in range (4)]
    while 1:
        print("1. 휴지통 출력")
        print("2. 연락처 복원")
        print("3. 휴지통 비우기")
        print("4. 메인화면 가기")
        
        str_recycle_bin = input("메뉴 선택: ")
        
        if str_recycle_bin in recycle_items:
            num_recycle_bin = int(str_recycle_bin)
            if num_recycle_bin == 1:
                print_contact(recycle_bin_list)
            elif num_recycle_bin == 2:
                restore_contact(contact_list, recycle_bin_list)
            elif num_recycle_bin == 3:
                recycle_bin_list = []
                print("휴지통을 전부 비웠습니다.")
            elif num_recycle_bin == 4:
                break
        else:
            print("다시 입력해주세요.")
    return recycle_bin_list    
        # try:
        #     num_recycle_bin = int(input("메뉴 선택: "))
        # except ValueError as e:
        #         print(e)
        #         print("다시 입력해주세요.\n")
        # else:
        #     break
        # finally:
        #     print("")
    
    

# 휴지통 복원 함수
def restore_contact(contact_list, recycle_bin_list):   
    num_recycle_bin = len(recycle_bin_list)
    recycle_bin_items = [str(i) for i in range(num_recycle_bin)]
    recycle_bin_items.append('-1')
    
    while 1:       
        if num_recycle_bin == 0:
            print("복원할 연락처가 없습니다.")
            break
        
        print_contact(recycle_bin_list)
        
        str_restore = input("복원할 연락처 번호 입력(종료 = -1):")
        
        if str_restore in recycle_bin_items:
            num_restore = int(str_restore)
            if num_restore >= 0 :
                contact_list.append(recycle_bin_list[num_restore])
                del recycle_bin_list[num_restore] 
                print("복원이 완료 되었습니다.")
                break
            else:
                print("이전 화면으로 이동합니다.")
                break
        else:
            print("다시 입력해주세요.\n")
    
        

# 정렬 함수 -> 검색과 출력 함수에 사용됨
def sort_contact(contact_list, num_sort):
    if num_sort == 1:
        new_contact_list = sorted(contact_list, key = lambda Contact: Contact.name)
    elif num_sort == 2:
        new_contact_list = sorted(contact_list, key = lambda Contact: Contact.phone_number)
    elif num_sort == 3:
        new_contact_list = sorted(contact_list, key = lambda Contact: Contact.e_mail)
    elif num_sort == 4:
        new_contact_list = sorted(contact_list, key = lambda Contact: Contact.addr)
    elif num_sort == 5:
        new_contact_list = sorted(contact_list, key = lambda Contact: Contact.group)
    elif num_sort == 6:
        new_contact_list = sorted(contact_list, key = lambda Contact: Contact.nickname)
    return new_contact_list

def print_menu():
    menu_items = [str(i + 1) for i in range (9)]
    while 1:
        print("=" * 4 + "메인 화면" + "=" * 4)
        print("1. 연락처 입력")
        print("2. 연락처 출력")
        print("3. 연락처 검색")
        print("4. 연락처 수정")
        print("5. 연락처 삭제")
        print("6. 연락처 저장")
        print("7. 즐겨찾기")
        print("8. 휴지통")
        print("9. 종료")
        print("=" * 15)
        menu = input("메뉴선택: ")
        if menu in menu_items:
            return int(menu)
        else:
            print("다시 입력해주세요.\n")
    # return int(menu)

def print_selection():
    print("1. Name")
    print("2. Phone Number")
    print("3. E-mail")
    print("4. Address")
    print("5. Group")
    print("6. Nickname")
    
def run():
    contact_list = [] # 사전구조 적용 (선택)
    recycle_bin_list = []
    bookmark_list = []

    sort_items = [str(i + 1) for i in range(len(Contact.items))]
    load_contact(contact_list, recycle_bin_list, bookmark_list)
    # 화면 추가할 것 : 검색 기능, 수정 기능 
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact(contact_list)
            contact_list.append(contact)
        elif menu == 2:
            while 1:
                print_selection()
                num_sort = input("정렬 방법 번호 선택: ")
                if num_sort in sort_items:
                    print_contact(sort_contact(contact_list, int(num_sort)))
                    break
                else:
                    print("다시 입력해주세요.")
        elif menu == 3:
            (dummy_list, dummy_index, num_search)= search_contact(contact_list)
            print_contact(sort_contact(dummy_list, num_search))
        elif menu == 4:
            update_contact(contact_list)
        elif menu == 5:
            delete_contact(contact_list, recycle_bin_list, bookmark_list)
        elif menu == 6:
            store_contact(contact_list, recycle_bin_list, bookmark_list)
            print("저장이 완료 되었습니다.")
        elif menu == 7:
            bookmark_contact(contact_list, bookmark_list)
        elif menu == 8:
            recycle_bin_list = recycle_bin(contact_list, recycle_bin_list)
        elif menu == 9:
            store_contact(contact_list, recycle_bin_list, bookmark_list)
            print("연락처 프로그램을 종료합니다.")
            break

#%% main()
run()




















