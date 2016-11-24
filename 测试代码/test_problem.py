# coding=utf-8 
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import re
import json
import unittest
import traceback

from colortest import ColorTestRunner


def readFile(fn):
    fp = file(fn)
    content = fp.read()
    fp.close()
    return content

content = readFile('qa_test.txt')


class ProblemTestCase(unittest.TestCase):
    ##初始化工作
    def setUp(self):
        pass

    # 退出清理工作
    def tearDown(self):
        pass

    # 具体的测试用例，一定要以test开头
    def test_parse_block(self):
        # printDeep(answers)
        json = [u'a', {}]
        r = check_process(json, answers[0], comments[0])
        #print 'result is ', r
        #printDeep(r, 0)
        self.assertEqual(r[0], True, "easiest case")
        
    def test_parse_block_2(self):
        json = [u'd', {u'a': u'a', u'c': u'c', u'b': u'b'}]
        r = check_process(json, answers[0], comments[0])
      # print 'result is ', r
      # printDeep(answers, 0)
      # printDeep(r, 0)
        self.assertEqual(r[0], True, "easiest case")
        
    def test_parse_block_3(self):
        json = [u'd', {u'a': u'a', u'c': u'c', u'b': u'b'}, [u'`x+y`', u'c']]
        r = check_process(json, answers[0], comments[0])
      # print 'result is ', r
        printDeep(r, 0)
        self.assertEqual(r[0], False, "easiest case")
        
    def test_parse_block_4(self):
        json = ['c', {'a': 'a'}]
        r = check_process(json, answers[0], comments[0])
      # printDeep(r, 0)
        self.assertEqual(r[0], False, "easiest case")

    def test_parse_block_full(self):
        json = ['Q.E.D.', {'a': 'a', 'b': 'cab', 'c': 'tempc',
            'd': 'determine', 'e': 'like'}]
        # printDeep(answers, 0)
        r = check_process(json, answers[0], comments[0])
     #  print len(answers)
     #  print answers
        r = list(r)
        #printDeep(answers, 0)
        #printDeep(r, 0)
     #  print len(answers), len(json[1])
        if r[0] and len(json) > 1 and len(json[1]) + 2 == len(answers[0]):
            r.append('完成')
        # printDeep(r, 0)
        self.assertEqual(r[0], True, "check process case full")
        self.assertEqual(r[3], '完成', "check process case full")

    def test_text_check_1(self):
        r = checkText('不知道', '')
        # printDeep(r, 0)
        self.assertEqual(r[0], True, "case 答案为空，全部通过")

  # def test_check_process(self):
  #     qa, slug = qa_parse(content)
  #     s1 = qa['answer'][1]
  #     s3 = qa['answer'][3]
  #     print type(s1)

  #     self.assertEqual(True, True, 'test check choice fail')

  # def test_check_process2(self):
  #     qa, slug = qa_parse(content)
  #     print qa['answer'][2]
  #     f, r = checkText('ae', qa['answer'][2][0])
  #     self.assertEqual(f, False, 'test check text fail')

  # def test_check_text_3(self):
  #     qa, slug = qa_parse(content)
  #     f, r = checkText('eg', qa['answer'][2][0])
  #     self.assertEqual(f, False, 'test check text fail %s' % r)

  # def test_check_text_4(self):
  #     qa, slug = qa_parse(content)
#       f, r = checkText('hg', qa['answer'][2][0])
#       self.assertEqual(f, True, 'test check text fail')


from markdown.extensions.problem import *
start = content.find("{%")
lists = []
while start >= 0 and start < len(content):

    end = find_right_next(content, start, 0, '\n')
    lists.append(content[start:end])
    start = content.find("{%", end)
    
t = renderQuestion(lists[1], 1)

#print dir(t)
#print t

if __name__=='__main__':
    #unittest.main(testRunner = ColorTestRunner())
    #unittest.main()
    pass
