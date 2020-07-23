import datetime
import math
import random
import time
import string

from datetime import date
from datetime import datetime
from string import ascii_uppercase

from lemoncheesecake.matching import check_that, equal_to


# from consumer.farmer.constant import CONSTANT_FILE_NAME


def generate_number_between(num1, num2):
    random_num = random.randrange(num1, num2)
    return random_num


def generate_float_number_between(num1, num2):
    random_float_num = random.uniform(num1, num2)
    floored_value = math.floor(random_float_num * 100) / 100.0
    return floored_value


def floor_two_decimals(num):
    floored_value = math.floor(num * 100) / 100.0
    return floored_value


def generate_number_of_length_n(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    random_number = random.randint(range_start, range_end)
    return random_number


def pick_random_list_item(my_list):
    random_element = random.choice(my_list)
    return random_element


def pick_random_dict_item(my_dict):
    random_element = random.choice(list(my_dict.keys()))
    return random_element


def generate_random_string(string_length=5):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(string_length)) + "_Automation"


def generate_random_string_of_length_n(n):
    random_string = ''.join(random.choice(ascii_uppercase) for i in range(n))
    return random_string


def generate_string_ending_with_number(string_starts_with):
    string = "{}{}".format(string_starts_with, random.randint(0, 100))
    return string


def generate_now_timestamp_rc3339():
    return datetime.now().isoformat('T')


def get_current_date_and_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")


def get_today_date():
    return str(date.today())


def get_current_time():
    return datetime.now().strftime("%H:%M:%S")


def get_utc_ms_time(value):
    try:
        date_obj = value
        if isinstance(value, str):
            date_obj = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        return int(time.mktime(date_obj.timetuple())) * 1000

    except:
        return ''


def get_utc_ms_time_old_order_format(value):
    try:
        date_obj = value
        if isinstance(value, str):
            date_obj = datetime.strptime(value, "%d %b %Y %H:%M")
        return int(time.mktime(date_obj.timetuple())) * 1000

    except Exception as e:
        print(e)
        return ''


def get_values_from_list(list_values, key):
    expected_values = []
    for values in list_values:
        expected_values.append(values.get(key))
    return expected_values


def get_date_time_obj(epoch_time):
    return datetime.fromtimestamp(epoch_time / 1000)


def remove_value_from_dict(my_dict, list_value):
    for value in list_value:
        my_dict.pop(value)
    return my_dict


def get_response_data_and_validate_response_code(response):
    check_that("response code", response.status_code, equal_to(200))
    return response.json()["responseData"]


def get_response_data_and_validate_response_code_for_negative_test(response):
    check_that("response code", response.status_code, equal_to(400))
    return response.json()["responseData"]


def get_current_time_in_utc():
    now = int(round(time.time() * 1000) + 5000)
    return now


def get_upcoming_time_in_utc(n):
    now = int(round(time.time() * 1000) + (60000 * n))
    return now


def get_back_date_time_in_utc(n):
    now = int(round(time.time() * 1000))
    next_Day_Time = now - n * (24 * 60 * 60 * 1000)
    return next_Day_Time


def get_next_date_time_in_utc(day):
    now = int(round(time.time() * 1000))
    next_Day_Time = now + day * (24 * 60 * 60 * 1000)
    return next_Day_Time

# def read_values_from_csv(csv_values):
#     config_path = os.path.join(project_dir, CONSTANT_FILE_NAME)
#     file = open(config_path, "r")
#     reader = csv.reader(file)
#     for line in reader:
#         csv_values[line[0]] = line[1]
#     return csv_values
