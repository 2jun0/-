import sys

def show_my_detail_score(path, my_num):

    f = open(path, 'r')
    student_score_tuples = []

    while True:
        line = f.readline()
        if not line:
            break

        # idx 0 : numbering
        # idx 1 : student number
        # idx 2 : score
        splited_line = line.split()
        student_score_tuples.append((splited_line[1], float(splited_line[2])))

    f.close()

    student_score_tuples = sorted(student_score_tuples, key=lambda student_score_tuple: student_score_tuple[1], reverse=True)

    my_place = None
    my_score = None
    place = 1
    num_at_place = 0
    sum_of_score = 0
    for idx, student_score_tuple in enumerate(student_score_tuples):
        # tuple idx 0 : student number
        # tuple idx 1 : score
        sum_of_score = sum_of_score + student_score_tuple[1]

        if student_score_tuples[idx-1][1] > student_score_tuple[1]:
            place = place + num_at_place
            num_at_place = 1
        else:
            num_at_place = num_at_place + 1

        if student_score_tuple[0] == my_num:
            my_place = place
            my_score = student_score_tuple[1]

        print('{:02d} 등\tnum : {}\tscore : {}'.format(place, student_score_tuple[0], student_score_tuple[1]))

    print('평균 점수 : {}'.format(sum_of_score/len(student_score_tuples)))

    print('\n당신의 등수 : {}\t당신의 점수 : {}'.format(my_place, my_score))
    my_rate = my_place/len(student_score_tuples)
    print('당신은 상위 {:05.2f}%로 \'{}\'입니다!'.format(my_rate*100, get_grade_point(my_rate, student_score_tuple[1])))


def get_grade_point(place ,score):
    if score == 0:
        return 'F'

    if place <= 0.3:
        return 'A0 ~ A+'
    elif place <= 0.7:
        return 'B0 ~ B+'
    else:
        return 'D0 ~ C+'


def main(args):
    file_path = './totalScore.txt'
    my_num = None

    if len(args) == 2:
        file_path = args[0]
        my_num = args[1]
    else:
        my_num = args[0]

    show_my_detail_score(file_path, my_num)

if __name__ == '__main__':
    main(sys.argv[1:])
