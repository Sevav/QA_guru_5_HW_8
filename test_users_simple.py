import csv


def test_workers_are_adults():
    with open('users.csv') as f:
        users = csv.DictReader(f, delimiter=';')
        workers = [user for user in users if user['status'] == 'worker']
    for worker in workers:
        assert int(worker['age']) >= 18