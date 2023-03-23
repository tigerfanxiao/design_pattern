'''
这个版本是基于callable来月约束函数
'''

import string
import random
from abc import ABCMeta, abstractmethod
from typing import List, Callable


def generate_id(length=8):
    # helper function to generate an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


# 不需要定义一个Strategy接口了

def fifo_ordering(tickets: List[SupportTicket]) -> List[SupportTicket]:
    return tickets.copy()


def filo_ordering(tickets: List[SupportTicket]) -> List[SupportTicket]:
    tickets_copy = tickets.copy()
    tickets_copy.reverse()  # 这个是直接在数组上操作的
    return tickets_copy


def random_ording(tickets:List[SupportTicket]) -> List[SupportTicket]:
    tickets_copy = tickets.copy()
    random.shuffle(tickets_copy)
    return tickets_copy  # 这个也是在数组上实现的


# 新增一个strategy
def blackhole_ordering(tickets: List[SupportTicket]) -> List[SupportTicket]:
    return []


class CustomerSupport:

    def __init__(self):
        self.tickets = []
        # 不应该在初始化的适合把strategy传进来，而是使用的时候才传进来

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, processing_strategy_fn: Callable[[List[SupportTicket]], List[SupportTicket]]):
        # create the ordered list
        ticket_list = processing_strategy_fn(self.tickets)

        # 在获取到ordered_list之后再校验
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        for ticket in ticket_list:
            self.process_ticket(ticket)  # 到此，如果增加新的strategy，这个函数不需要变化
    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


if __name__ == '__main__':
    app = CustomerSupport()

    # register a few tickets
    app.create_ticket("John Smith", "My computer makes strange sounds!")
    app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
    app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

    # process the tickets
    app.process_tickets(blackhole_ordering)
