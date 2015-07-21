#!/usr/bin/env python
# coding=utf-8

'''
github: https://github.com/gitferry/
author: Fangyu Gai <gaigai508@gmail.com>
To create new problems including python surce file and mark down file
'''

import os
from datetime import date

def create_new_problem(problem_name):
	name_words = problem_name.split(' ')
	url_name = '-'.join(name_words).lower()
	short_name = problem_name.replace(' ', '')

	os.mkdir('./algorithms/' + short_name)

	md_file = file(os.path.join(short_name, short_name+'.md'), 'w')
	md_content = \
	'''# [%s](https://leetcode.com/problems/%s/)

---

## Description

---

---

代码实现：[%s](./%s.py)
	''' % (problem_name, url_name, problem_name, short_name)


	md_file.write(md_content)
	md_file.close()

	current_date = date.today()

	py_file = file(os.path.join(short_name, short_name+'.py'), 'w')
	py_content = \
	'''#!/usr/bin/env python
# coding=utf-8
\'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : %s
\'''
''' % (current_date.strftime("%d/%m/%Y"))
	py_file.write(py_content)
	py_file.close()


if __name__ == '__main__':
	problem_name = raw_input('Please input the name of the problem:\n')
	create_new_problem(problem_name)




