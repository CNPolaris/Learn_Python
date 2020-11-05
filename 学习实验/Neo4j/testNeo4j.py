# -*- coding: utf-8 -*-
# @Time    : 2020/11/5 20:20
# @FileName: testNeo4j.py
# @Author  : CNPolaris

from py2neo import Graph, Node, Relationship, NodeMatcher
import pandas as pd


def importRelation():
    # 连接Neo4j图数据库
    graph = Graph('http://localhost:7474', usename='neo4j', password='tianxin')
    # 文件位置以及测试
    file_path = './果部.csv'
    file = pd.read_csv(file_path)
    print(file.head())
    # for index,row in file.iterrows():
    #     print(row['name'])
    for index, row in file.iterrows():
        name = row['name']
        alias = row['alias']
        smell = row['smell']
        cure = row['cure']
        part = '果类'
        part_node = Node('部类', name=part)
        med_node = Node('中药', name=name)
        alias_node = Node('别名', name=alias)
        smell_node = Node('气味品质', name=smell)
        cure_node = Node('主治方法', name=cure)
        relat_part = Relationship(med_node, '属于', part_node)
        relat_alias = Relationship(med_node, '别名是', alias_node)
        relat_smell = Relationship(med_node, '气味品质是', smell_node)
        relat_cure = Relationship(med_node, '使用方法是', cure_node)
        graph.create(relat_part)
        graph.create(relat_alias)
        graph.create(relat_smell)
        graph.create(relat_cure)
        graph.merge(part_node, "部类", "果类")

        print(index)


importRelation()
