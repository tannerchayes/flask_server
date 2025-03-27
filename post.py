import csv


def get_post(post_id):
    with open('data.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if post_id == row['id']:
                return row

def get_about(about_id):
    with open('about.csv', 'r', encoding='utf-8') as about_file:
        read_csv = csv.DictReader(about_file)

        for row in read_csv:
            if about_id == row['about']:
                return row
