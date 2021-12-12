# -*- coding: utf-8 -*-
# @Time    : 5/19/20 11:15 AM
# @Author  : WEY
# @File    : convert_xml
# @Software: PyCharm
# !/usr/bin/python3
# -*- coding:utf-8 -*-
'''
 convert mrsa xml to the formate of    ' I  B-PERSON '
'''
import xml.etree.ElementTree as ET


# 从xml文件中读取，用getroot获取根节点，根节点也是Element对象
# def process_xml_to_ontonotes(source_path, target_path):  # change  xml to the format of  ontonotes
#     count_sentence = 0
#     type_str = ''
#     list_type = []
#     tree = ET.parse(source_path)
#     root = tree.getroot()
#     # print(root)
#     # print(root.tag,root.text)
#     with open(target_path, 'w', encoding='utf-8') as precess_text:
#         for child in root:  # root is text
#             for i in child:  # child is sentence,i is w
#                 # print(i.text, i.tag, i.attrib, i.tail)
#                 if i.text is not None:
#                     o_list = list(i.text)
#                     for char in o_list:
#                         precess_text.write(char + '\t' + 'O' + '\n')
#                 else:
#                     for j in i:  # i is w ,so j is NaMEX     <NAMEX TYPE="ORGANIZATION">中共中央</NAMEX>
#                         if j.attrib.get('TYPE') == 'PERSON' or j.attrib.get('TYPE') == 'LOCATION' or j.attrib.get(
#                                 'TYPE') == 'ORGANIZATION':
#                             char_list = list(j.text)
#                             char_len = len(char_list)
#                             print(str(char_len) + "\n")
#                             if char_len == 1:
#                                 precess_text.write(char_list[0] + '\t' + 'B-' + j.attrib.get('TYPE') + '\n')
#                             elif char_len > 1:
#                                 for index in range(char_len - 1):
#                                     if index == 0:
#                                         precess_text.write(char_list[0] + '\t' + 'B-' + j.attrib.get('TYPE') + '\n')
#                                     if char_len > 1:
#                                         precess_text.write(
#                                             char_list[index + 1] + '\t' + 'I-' + j.attrib.get('TYPE') + '\n')
#                             #  print(j.text,j.tag,j.attrib.get('TYPE'),j.tail)
#                             #  中共中央 NAMEX {'TYPE': 'ORGANIZATION'} None   <w><NAMEX TYPE="ORGANIZATION">中共中央</NAMEX></w>
#                             list_type.append(j.attrib.get('TYPE'))
#             precess_text.write('\n')
#             count_sentence = count_sentence + 1
#     set_types = set(list_type)
    # f = open("./output_result/coun_train_mrsa.txt", 'w')
    # i = 0
    # for one in set_types:
    #     i = i + 1
    #     num_type = list_type.count(one)
    #     f.write(str(i) + ":the type is " + one + ":" + str(num_type) + "\n")
    #     print(str(i) + "the type is " + one + ":" + str(num_type))  # count the num of   every kind of type for mrsa
    #     f.close()

    # print('The number of sentence is:')
    # print(count_sentence)
    # print('The number of typ is:')
    # print(len(set_types))

# 4 columns
# def count_enity(source_path, target_path):  # count the num  of mrsa.test.net's enities
#     with open(source_path, 'r+', encoding='utf-8') as file:
#         tag = 1
#         sentence_num = 0
#         enity_list = []
#         for line in file:
#             line_list = line.split()
#             line_len = len(line_list)
#             if line_len == 0 and tag == 1:  # note: 'else' is logic error ,'elif' is correct
#                 tag = 0
#                 sentence_num = sentence_num + 1
#             elif line_len == 4:
#                 tag = 1
#                 if line_list[3] not in 'O':
#                     if line_list[3].__contains__('B-'):
#                         enity_list.append(line_list[3])
#             elif line_len != 0:
#                 tag = 1
#     enity_set = set(enity_list)
#     f = open(target_path, 'w')
#     i = 0
#     for one in enity_set:
#         i = i + 1
#         num_type = enity_list.count(one)
#         f.write(str(i) + ":the type is " + one + ":" + str(num_type) + "\n")
#     sentence_actual = sentence_num - 1
#     f.write('The number of sentences:' + str(sentence_actual) + '\n')
#     f.write('The num of enity:' + str(len(enity_list)) + '\n')
#     f.write('The kinds of enity:' + str(len(set(enity_list))) + '\n')
#     f.write('the dataset is :' + source_path + '\n')
# tow columns
def count_enity(source_path, target_path):  # count the num  of mrsa.test.net's enities
    with open(source_path, 'r+', encoding='utf-8') as file:
        tag = 1
        sentence_num = 0
        enity_list = []
        for line in file:
            line_list = line.split()
            line_len = len(line_list)
            if line_len == 0 and tag == 1:  # note: 'else' is logic error ,'elif' is correct
                tag = 0
                sentence_num = sentence_num + 1
            elif line_len == 2:
                tag = 1
                if line_list[1] not in 'O':
                    if line_list[1].__contains__('B-'):
                        enity_list.append(line_list[1])
            elif line_len != 0:
                tag = 1
    enity_set = set(enity_list)
    f = open(target_path, 'w')
    i = 0
    for one in enity_set:
        i = i + 1
        num_type = enity_list.count(one)
        f.write(str(i) + ":the type is " + one + ":" + str(num_type) + "\n")
    sentence_actual = sentence_num - 1
    f.write('The number of sentences:' + str(sentence_actual) + '\n')
    f.write('The num of enity:' + str(len(enity_list)) + '\n')
    f.write('The kinds of enity:' + str(len(set(enity_list))) + '\n')
    f.write('the dataset is :' + source_path + '\n')
    f.close()



if __name__ == '__main__':
    # process_xml_to_ontonotes('msra/msra_bakeoff3_test.xml', './output_result/msra.test.ner')
    # process_xml_to_ontonotes('msra/msra_bakeoff3_training.xml', './output_result/msra.train.ner')


    # count_enity("ontonotes_5.0/onto.test.ner","./output_result/coun_test_notonotes.txt")
    # count_enity("msra/mrsa.development.ner","./output_result/count_development_mrsa.txt")
    # count_enity("../weiboNER_2nd_conll/weiboNET_2nd_conll.dev.resust", "../weiboNER_2nd_conll/weiboNER_2nd.dev.txt")
    # count_enity("../weiboNER_2nd_conll/weiboNET_2nd_conll.test.resust", "../weiboNER_2nd_conll/weiboNER_2nd.test.txt")
    # count_enity("../weiboNER_2nd_conll/weiboNET_2nd_conll.train.resust", "../weiboNER_2nd_conll/weiboNER_2nd.train.txt")
    # for i in range(0):
    #      print(i)
    # str = '中共中央'
    # list_str = list[str]
    # # i = str.split()
    # print(list_str)
    # count_enity("/home/zutnlp/data/LDC/result/english/new_test.bio", "/home/zutnlp/data/LDC/result/english/new_test.bio.result")
    count_enity("/home/zutnlp/wueryong/LDC/result/english/new_test.bio","/home/zutnlp/wueryong/LDC/result/new_test.bio.result")
    pass
