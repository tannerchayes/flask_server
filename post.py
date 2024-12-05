import csv


def get_post(post_id):
    with open('data.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if post_id == row['id']:
                return row

