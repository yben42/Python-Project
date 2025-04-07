from datetime import date
from datetime import datetime
class Passport:
    passport_count = 0  # Class variable to track the number of passports created

    def __init__(self, first_name, last_name, dob, country, exp_date):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = datetime.strptime(dob, "%Y-%m-%d").date()
        self.country = country
        self.exp_date = datetime.strptime(exp_date, "%Y-%m-%d").date()
        self.stamps = {}  # Dictionary to track countries visited and their counts
        self.passport_id = Passport.passport_count
        Passport.passport_count += 1

    def is_valid(self):
        return self.exp_date > date.today()

    def summary(self):
        validity = 'valid' if self.is_valid() else 'expired'
        return (f"This passport belongs to {self.first_name} {self.last_name}, born on {self.dob} "
                f"in {self.country}. It is {validity}.")

    def check_data(self, first_name, last_name, dob, country):
        valid_dob = datetime.strptime(dob, "%Y-%m-%d").date()
        return (self.first_name == first_name and
                self.last_name == last_name and
                self.dob == valid_dob and
                self.country == country and
                self.is_valid())

    def stamp(self, country_name):
        if country_name != self.country:
            self.stamps[country_name] = self.stamps.get(country_name, 0) + 1

    def countries_visited(self):
        return list(self.stamps.keys())

    def times_visited(self, country_name):
        return self.stamps.get(country_name, 0)

    def sum_square_visits(self):
        return sum(count ** 2 for count in self.stamps.values())

    def passport_number(self):
        return self.passport_id

if __name__ == "__main__":
    ben = Passport("Ben", "Yiu", "1997-04-16", "U.S.A.", "3000-10-31")
    print(ben.summary())  
    #Output: This passport belongs to Ben Yiu, born on 1997-04-16 in U.S.A.. It is valid.

#if __name__ == "__main__":
       #alan = Passport(
            #"Alan", 
            #"Turing", 
            #"1912-06-23", 
            #"The United Kingdom", 
            #"1954-06-07"
        #)
       #print("Alan is valid", alan.is_valid())
       #should output: False

       #print(alan.summary())
       #should output: This passport belongs to Alan Turing, born on 1912-06-23 in The United Kingdom. It is invalid.

       #codegrade = Passport(
            #"Code", 
            #"Grade", 
            #"2017-07-21", 
            #"The Netherlands", 
            #"2999-12-31"
        #)

       #print(codegrade.check_data("Code", "Grade", "2017-07-21", "The Netherlands"))
       #should output: True
       #it printed everything correctly - Ben
