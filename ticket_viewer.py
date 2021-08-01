import requests
from datetime import datetime, timedelta
from numpy import array_split
from math import ceil


def get_request(access_token):
    return requests.get('https://zccachopra.zendesk.com/api/v2/tickets', auth=('chopra21@purdue.edu/token', access_token))


def get_data(request):
    return request.json()


def get_all_tickets(json):
    tickets = []
    for ticket in json['tickets']:
        time = (datetime.strptime(ticket['created_at'], '%Y-%m-%dT%H:%M:%SZ') - timedelta(hours=8)).strftime(
            '%b %d, %Y at %-I:%M %p')
        tickets.append(
            f"Ticket #{ticket['id']} with subject '{ticket['subject']}' opened by {ticket['requester_id']} and requested by {ticket['submitter_id']} on {time} has a status of {ticket['status']}.")

    num_pgs = ceil(len(tickets) / 25)
    tickets = array_split(tickets, num_pgs)
    return tickets


def get_ticket(json, tick_num):
    for ticket in json['tickets']:
        if ticket['id'] == tick_num:
            time = (datetime.strptime(ticket['created_at'], '%Y-%m-%dT%H:%M:%SZ') - timedelta(hours=8)).strftime(
                '%b %d, %Y at %-I:%M %p')
            tick = f"Ticket #{ticket['id']} with subject '{ticket['subject']}' opened by {ticket['requester_id']} and requested by {ticket['submitter_id']} on {time} has a status of {ticket['status']}."
            return tick
    return None


def main():
    access_token = 'VNShXh0CtsAEU9z0v47cTKmSSSU8jnCHaSAxKmgn'
    r = get_request(access_token)
    if r.status_code != 200:
        print(f'There is an error with the API request. Status code: {r.status_code}!')
        return

    data = get_data(r)

    print('Welcome to the ticket viewer menu. You have the following options:')
    print('\t1. Enter "1" to view all tickets.')
    print('\t2. Enter "2" to view a particular ticket.')
    print('\t3. Enter "q" to quit.')

    option = input()
    print()

    while True:
        if option == 'q':
            print('Thanks for using the ticket viewer!')
            break

        elif option == '1':
            tickets = get_all_tickets(data)
            page = 1
            while True:
                print(f'Viewing page {page} of {len(tickets)}')
                print()
                for ticket in tickets[page - 1]:
                    print(ticket)

                try:
                    print()
                    page_inp = int(input('Enter another page number to view, or "0" to return to the main menu: '))
                    if page_inp == 0:
                        print()
                        break
                    elif page_inp < 1 or page_inp > len(tickets):
                        print()
                        print(f'Error: Invalid page number! There are only {len(tickets)} pages.')
                        print()
                    else:
                        page = page_inp

                except ValueError:
                    print()
                    print('Error: Page number has to be numeric!')
                    print()

        elif option == '2':
            try:
                tick_num = int(input('Enter a ticket number: '))
                ticket = get_ticket(data, tick_num)

                if ticket:
                    print()
                    print(ticket)
                else:
                    print()
                    print('Error: Ticket does not exist!')

            except ValueError:
                print()
                print('Error: Invalid Ticket Number!')
                print()
                continue

            print()

        else:
            print('Error: Invalid option!')
            print()

        print('Welcome to the ticket viewer menu. You have the following options:')
        print('\t1. Enter "1" to view all tickets.')
        print('\t2. Enter "2" to view a particular ticket.')
        print('\t3. Enter "q" to quit.')

        option = input()
        print()


if __name__ == '__main__':
    main()
