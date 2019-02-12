import csv

from core.models import Entity, Question, Evaluation


def read_csv_file(file_path):
    with open('data/Contact_List.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print(row[1])


def save_entity_list():
    with open('core/data/Old_Contact_List.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # print()  # skip the headers
        # header = next(readCSV, None)
        for row in readCSV:
            print(row)
            entity = Entity(entity_name=row[1], region_name=row[0], mcp_name=row[2])
            entity.save()


def save_questions_lcps():
    with open('core/data/LCP_Data.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        # print()  # skip the headers
        header = next(readCSV, None)

        for row in readCSV:

            entity = Entity.objects.get(entity_name=row[0])

            evaluation = Evaluation(type=2, number_of_responses=row[16], entity=entity)
            evaluation.save()
            create_question(header[1], row[1], evaluation)
            create_question(header[2], row[2], evaluation)
            create_question(header[3], row[3], evaluation)
            create_question(header[4], row[4], evaluation)
            create_question(header[5], row[5], evaluation)
            create_question(header[6], row[6], evaluation)
            create_question(header[7], row[7], evaluation)
            create_question(header[8], row[8], evaluation)
            create_question(header[9], row[9], evaluation)
            create_question(header[10], row[10], evaluation)
            create_question(header[11], row[11], evaluation)
            create_question(header[12], row[12], evaluation)
            create_question(header[13], row[13], evaluation)
            create_question(header[14], row[14], evaluation)
            create_question(header[15], row[15], evaluation)

            print("Entity " + entity.entity_name + ' parsed successfully.')


def save_questions_mcvps():
    with open('core/data/MCVP_Data.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        # print()  # skip the headers
        header = next(readCSV, None)

        for row in readCSV:
            entity = Entity.objects.get(entity_name=row[0])
            evaluation = Evaluation(type=1, number_of_responses=row[20], entity=entity)
            evaluation.save()
            create_question(header[1], row[1], evaluation)
            create_question(header[2], row[2], evaluation)
            create_question(header[3], row[3], evaluation)
            create_question(header[4], row[4], evaluation)
            create_question(header[5], row[5], evaluation)
            create_question(header[6], row[6], evaluation)
            create_question(header[7], row[7], evaluation)
            create_question(header[8], row[8], evaluation)
            create_question(header[9], row[9], evaluation)
            create_question(header[10], row[10], evaluation)
            create_question(header[11], row[11], evaluation)
            create_question(header[12], row[12], evaluation)
            create_question(header[13], row[13], evaluation)
            create_question(header[14], row[14], evaluation)
            create_question(header[15], row[15], evaluation)
            create_question(header[16], row[16], evaluation)
            create_question(header[17], row[17], evaluation)
            create_question(header[18], row[18], evaluation)
            create_question(header[19], row[19], evaluation)

            print("Entity " + entity.entity_name + ' parsed successfully.')


def create_question(header, score, evaluation):
    question = Question(question_text=header, score=score, evaluation=evaluation)
    question.save()
