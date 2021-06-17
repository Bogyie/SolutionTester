import time
import subprocess


class SolutionTester:
    def __init__(self, chk=True, time_lim=1.0, mem_lim=512):
        """
        :param chk: Solution test progress
        :param time_lim: Time limit (Second)
        :param mem_lim: Memory limit (MB)
        """
        self.chk = chk
        self.time_lim = time_lim
        self.mem_lim = mem_lim
        self.test_data = {}
        self.path = './solution.py'

    def set_cases_terminal(self, case_num=1):
        """
        :param case_num: Volume of test cases
        """
        for i in range(case_num):
            print(f'- Test Case #{i+1} -\nPlease enter example input')
            input_lines = ''
            while True:
                line = input()
                if line:
                    input_lines += line + '\n'
                else:
                    break

            print(f'- Test Case #{i + 1} -\nPlease enter example output')
            output_lines = ''
            while True:
                line = input()
                if line:
                    output_lines += line + '\n'
                else:
                    break
            self.test_data[input_lines] = output_lines

    def set_cases_dict(self, cases:dict):
        """
        :param cases: { test_input : test_output }
            example : { "1 2 3\n4 5 6\n": "5\n" }
        :return:
        """
        self.test_data = cases

    def set_solution(self, where='./solution.py'):
        """
        :param where: solution file path
        """
        self.path = where

    def start_test(self):
        result = []
        for test_input, test_output in self.test_data.items():

            time_st = time.time()

            func_result = subprocess.run(['python', self.path], input=test_input, text=True, capture_output=True)

            time_ed = time.time()

            func_stdout = func_result.stdout
            total_time = round(time_ed - time_st, 6)

            if total_time <= self.time_lim and func_stdout == test_output:
                result.append(['Pass', total_time, func_stdout])
            else:
                result.append(['False', total_time, func_stdout])

        return result


