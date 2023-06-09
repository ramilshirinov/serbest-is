"""
    1) Istifadeciye secim, zeng etmek isteyirsiz yoxsa ad axtarmaq:
    2) data baza: dictionaryden ibaret list:
    3) nomrenin validasiyasini yoxlamaq:
    4) nomrenin kantaktinda olub olmamasini yoxlamaq, eger varsa "siz filan adli adama zeng edirsiz" mesaji qaytarmaq, 
        eger yoxsa 'nomre'- zeng edir zeng edirsiz mesaj:
    5) Ada gore nomre axtarmaq:
    6)davam etmek istemirem proqram diyanacaq
"""

from pprint import pprint
validate_number = "+994556375118"

Database_Ramil = [
    {"name":"Tamerlan", "number":"+994556375118", "provider":"Bakcell"},
    {"name":"Ramil", "number":"+994552555555", "provider":"Bakcell"},
    {"name":"Elekber", "number":"+994552555555", "provider":"Bakcell"},
    {"name":"tAmerlan", "number":"+994555123675", "provider":"Bakcell"},
]
provider_lists = [
    {"num":"+99455", "provider":"Bakcell"},
    {"num":"+99450", "provider": "Azercell"},
    {"num":"+99470", "provider": "Nar"},
    {"num":"+99477", "provider": "NAR"},
]
pvdl = ["+99455", "+99450", "+99470", "+99477"]

def validate_number_for_zero(number: str):
    if number.isdigit() and len(number) == 10 and int(number[0]) == 0:
        return True
    return False



def validate_number_for_country_code(number: str) -> bool:
    if len(number) == len(validate_number) and number[0:4]=="+994" and number[4::].isdigit():
        return True
    return False


def select_provider(number: int):

    if number[0:6] not in pvdl:
        print("This provider is false")

    else:

        for provider in range(len(provider_lists)):
            if provider_lists[provider]['num'] == number[0:6]:
                
                return provider_lists[provider]["provider"]



def add_contact(name: str, number: str, data: list) -> None:
    if validate_number_for_zero(number) or validate_number_for_country_code(number):
        contact={}
        contact["name"]=name
        if number[0] == "0":
            contact["number"] = "+994" + number[1::]
            contact["provider"] = select_provider(contact["number"])

        else:
            contact["number"] = number  
            contact["provider"] = select_provider(contact["number"])
        data.append(contact.copy())
        print("Successful operation")

    else:
        print("The number was not entered correctly")


def search_by_name(data: list) -> None:
    search_name=input("search_name: ")
    searched = False
    for sub in data:
        if sub['name'].lower() == search_name.lower():

            searched = True
            print("searched contact : " + str(sub))

    if searched == False:
        print("Contact not found")

    else:
        return search_by_name


def search_by_number(data: list) -> None:
    search_number=input("search_number: ")
    test_number = search_number
    searched = False
    if search_number[0] == "0" and len(search_number)==len("0556375118"):
        search_number = "+994" + search_number[1::]
        for sub in data:
            if sub['number'] == search_number:
                searched = True
                print("searched contact : " + str(sub))
                break
        if searched == False:
            print("Contact not found")

    else:
        print("TAMERLAN")

        for sub in data:
            if test_number in sub['number']:
                print("searched contact : " + str(sub))


# Ada gore istifadeci sayi tapir. 
def search_for_call_by_name(name: str, data: list) -> int:
    searched = False 
    user_count = 0
    for sub in data:
        if sub['name'].lower() == name.lower():
            searched = True
            user_count+=1

    if searched == False:
        print("Contact not found")

    return user_count

def call_by_name(name: str, data: list):
    
    if search_for_call_by_name(name=name, data=data) > 1:
        print("Which user do you want to call?: ")
        searched = False

        #Axtarılan istifadəçilərin siyahısı
        for sub in data:
            if sub['name'].lower() == name.lower():
                searched = True
                print("searched contact : " + str(sub))

        name = input("Enter name: ")
        searched = False

        for sub in data:
            if sub['name'] == name:
                searched = True
                print("called number : " + sub["number"])
                break

        if searched == False:
            print("Contact not found")


    elif search_for_call_by_name(name=name, data=data) == 1:
        for sub in data:
            if sub['name'] == name:
                searched = True
                print("called number : " + sub["number"])
                break

        if searched == False:
            print("Contact not found")
    
    else:
        print("There is no such contact")

def call_by_number(number: str, data: list):
    if number[0] == "0":
        number = "+994" + number[1::]

    for sub in data:
        if number == sub["number"]:
            print("called user : " + sub["name"])
            break

        else: print("An anonymous number is called")

# 1--select_call
# 2--select_search
# 3--select_create_contact
def main():
    proces_list = [
        {"1": "call"},
        {"2": "search"},
        {"3": "create contact"}
    ]

    for i in proces_list:
        print(i)

    while True:

        proces = input("Select the mentioned process: ")
        if proces == '1':
            proces_select = input("name or number: ")
            if proces_select == "name":
                name = input("write name: ")
                call_by_name(name, Database_Ramil)
            else:
                number = input("write number: ")
                call_by_number(number, Database_Ramil)

        if proces == '2':
            proces_select = input("name or number: ")
            if proces_select == "name":

                search_by_name(Database_Ramil)

            else:
                search_by_number(Database_Ramil)

        if proces == '3':
            name = input('write user name: ')
            number = input('write user number: ')
            add_contact(name=name, number=number, data=Database_Ramil)
            pprint(Database_Ramil)
        proceed = input("Are you want to continue: yes or not: ")
        if proceed == 'yes':
            continue
        elif proceed == 'not':
            break
        else:
            print('Proceed not correct')
            proceed = input("Are you want to continue: yes or not: ")
            if proceed == 'yes':
                continue
            elif proceed == 'not':
                break
main()