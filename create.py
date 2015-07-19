#!/usr/bin/env python
# coding=utf-8

'''
github: https://github.com/gitferry/
author: Fangyu Gai <gaigai508@gmail.com>
To create new problems including python surce file and mark down file
'''

import os

def create_new_problem(problem_name):
	name_words = problem_name.split(' ')
	url_name = '-'.join(name_words)
	short_name = problem_name.replace(' ', '')

	os.mkdir(short_name)

	md_file = file(os.path.join(short_name, short_name+'.md'), 'w')
	md_content = \
	'''# [%s](https://leetcode.com/problems/%s/)

---

## Description

---

---
	''' % (problem_name, url_name)
	md_file.write(md_content)
	md_file.close()

	py_file = file(os.path.join(short_name, short_name+'.py'), 'w').close()


if __name__ == '__main__':
	problem_name = raw_input('Please input the name of the problem:\n')
	create_new_problem(problem_name)




