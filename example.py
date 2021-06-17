from algo_tester import SolutionTester

# 백준 14719 빗물
# https://www.acmicpc.net/problem/14719

test_case = {
    '''4 4
3 0 1 4''': '5\n',
    '''4 8
3 1 2 3 4 1 1 2''': '5\n',
    '''3 5
0 0 0 2 0''': '0\n'
}

test = SolutionTester(True, 1.0, 256)
test.set_cases_dict(test_case)
print(test.start_test())
