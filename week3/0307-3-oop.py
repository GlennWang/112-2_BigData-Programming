import random

class Invoice:
    def __init__(self, number):
        self.number = number

class PrizeChecker:
    def __init__(self, special_prize):
        self.special_prize = special_prize
        self.invoices = []

    def generate_invoices(self, num_invoices=10000):
        for _ in range(num_invoices):
            invoice_number = random.randint(10000000, 99999999)
            self.invoices.append(Invoice(invoice_number))

    def check_prizes(self):
        special_prize_winners = []
        second_prize_winners = []
        third_prize_winners = []
        fourth_prize_winners = []
        fifth_prize_winners = []
        sixth_prize_winners = []

        for invoice in self.invoices:
            if invoice.number == self.special_prize:
                special_prize_winners.append(invoice)
            elif str(invoice.number)[-7:] == str(self.special_prize)[-7:]:
                second_prize_winners.append(invoice)
            elif str(invoice.number)[-6:] == str(self.special_prize)[-6:]:
                third_prize_winners.append(invoice)
            elif str(invoice.number)[-5:] == str(self.special_prize)[-5:]:
                fourth_prize_winners.append(invoice)
            elif str(invoice.number)[-4:] == str(self.special_prize)[-4:]:
                fifth_prize_winners.append(invoice)
            elif str(invoice.number)[-3:] == str(self.special_prize)[-3:]:
                sixth_prize_winners.append(invoice)

        total_invoices = len(self.invoices)

        print("特別獎中獎人數: {}，佔比: {:.2%}".format(len(special_prize_winners), len(special_prize_winners)/total_invoices))
        print_invoices("中獎發票號碼:", special_prize_winners)

        print("\n二獎中獎人數: {}，佔比: {:.2%}".format(len(second_prize_winners), len(second_prize_winners)/total_invoices))
        print_invoices("中獎發票號碼:", second_prize_winners)

        print("\n三獎中獎人數: {}，佔比: {:.2%}".format(len(third_prize_winners), len(third_prize_winners)/total_invoices))
        print_invoices("中獎發票號碼:", third_prize_winners)

        print("\n四獎中獎人數: {}，佔比: {:.2%}".format(len(fourth_prize_winners), len(fourth_prize_winners)/total_invoices))
        print_invoices("中獎發票號碼:", fourth_prize_winners)

        print("\n五獎中獎人數: {}，佔比: {:.2%}".format(len(fifth_prize_winners), len(fifth_prize_winners)/total_invoices))
        print_invoices("中獎發票號碼:", fifth_prize_winners)

        print("\n六獎中獎人數: {}，佔比: {:.2%}".format(len(sixth_prize_winners), len(sixth_prize_winners)/total_invoices))
        print_invoices("中獎發票號碼：", sixth_prize_winners)

def print_invoices(title, invoices):
    print(title, end = "")
    for invoice in invoices:
        print(invoice.number,end = ", ")
    print()
        


special_prize_number = 63603594
prize_checker = PrizeChecker(special_prize_number)
prize_checker.generate_invoices()
prize_checker.check_prizes()
