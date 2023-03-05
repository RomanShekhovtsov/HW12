from faker import Factory
import json

fake = Factory.create("uk_UA")

users = []


def create_users(fake, users: list, n=10):
    for _ in range(n):
        user = {}
        user["name"] = fake.name()
        user["phone"] = fake.phone_number()
        user["email"] = fake.email()
        user["birthday"] = fake.date()
        users.append(user)


class AddressBook():
    def __init__(self):
        self.users = users
        self.quantity = 2
        self.offset = 0
        self.word = None

    def to_json(self):
        with open("AddressBook.txt", "w", encoding='utf8') as fh:
            json.dump(self.users, fh, indent=4, ensure_ascii=False)
            print("Users were saved")

    def with_json(self):
        with open("AddressBook.txt", "r", encoding='utf8') as fh:
            unpacked = json.load(fh)
            return unpacked

    def __next__(self):
        end_value = self.offset + self.quantity
        page = self.users[self.offset:end_value]
        self.offset = end_value
        if self.offset > len(self.users):
            raise StopIteration

        if self.word:
            for us_dict in page:
                if self.word.casefold() in us_dict["name"].casefold() or self.word in us_dict["phone"]:
                    # print (us_dict)
                    return us_dict

        else:

            return page

    def __iter__(self):
        return self


if __name__ == "__main__":
    create_users(fake, users, n=5)
    ad_book = AddressBook()
    # print (ad_book)
    # print(ad_book.with_json())
    ad_book.quantity = 5
    ad_book.word = "Ол"
    print(next(ad_book))