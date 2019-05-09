import sys

def show_my_detail_score(my_score, my_rank, num):

    print('\n당신의 등수 : {}\t당신의 점수 : {}'.format(my_rank, my_score))
    my_rate = my_rank / num
    print('당신은 상위 {:05.2f}%로 \'{}\'입니다!'.format(my_rate*100, get_grade_point(my_rate, my_score)))

def predict_and_show_my_detail_score(my_score, median, max_score):

    # median값이 score band의 가운데값이 되게 만듦.
    # 허나, 만약 my_score가 너무 크거나 작다면 그에 따라 조절
    if median*2 <= max_score:
        max_score = median*2
        min_score = 0
    elif median*2 > max_score:
        min_score = 2*median - max_score

    if my_score > max_score:
        my_rate = 1
    elif my_score < min_score:
        my_rate = 100
    else:
        my_rate = 1 - (max_score - min_score) / my_score

    print('당신은 상위 {:05.2f}%로 \'{}\'입니다!'.format(my_rate*100, get_grade_point(my_rate, my_score)))


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
    operation_type = float(args[0])

    if operation_type == 0:
        my_score = float(args[1])
        my_rank = float(args[2])
        num = float(args[3])
        show_my_detail_score(my_score, my_rank, num)
    elif operation_type == 1:
        my_score = float(args[1])
        median = float(args[2])
        max_score = float(args[3])
        predict_and_show_my_detail_score(my_score, median, max_score)

if __name__ == '__main__':
    main(sys.argv[1:])
