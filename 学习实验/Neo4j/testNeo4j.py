# -*- coding: utf-8 -*-
# @Time    : 2020/11/5 20:20
# @FileName: testNeo4j.py
# @Author  : CNPolaris

from py2neo import Graph, Node, Relationship, NodeMatcher
import pandas as pd
import os

graph = Graph('bolt://localhost:7687', usename='neo4j', password='tianxin')


def importRelation():
    # 连接Neo4j图数据库
    """
    Neo4j+Python构建中药知识图谱测试
    """
    path = './data'
    files = os.listdir(path)
    # 创建根节点，以此开始
    node = Node('中药百部', name='中药百部')
    for file in files:
        if not os.path.isdir(file):  # 只打开文件
            data = pd.read_csv(path + '/' + file)
            part = file.split('.')[0]
            part_node = Node('部类', name=part)  # 为部类添加标签和名称
            for index, row in data.iterrows():
                name = row['name']
                alias = row['alias']
                smell = row['smell']
                cure = row['cure']
                med_node = Node('中药', name=name)    # 添加属性
                alias_node = Node('别名', name=alias)
                smell_node = Node('气味品质', name=smell)
                cure_node = Node('主治方法', name=cure)
                relat_part = Relationship(med_node, '属于', part_node)    # 添加关系
                relat_alias = Relationship(med_node, '别名是', alias_node)
                relat_smell = Relationship(med_node, '气味品质是', smell_node)
                relat_cure = Relationship(med_node, '使用方法是', cure_node)
                graph.create(relat_part)
                graph.create(relat_alias)
                graph.create(relat_smell)
                graph.create(relat_cure)
                print(index)
            relat_part_node = Relationship(part_node, "从属于", node)
            graph.create(relat_part_node)
            graph.merge(part_node, "部类", part)  # 创建节点


importRelation()
# res = graph.run("MATCH (n) RETURN n WHERE ").data()
# links = graph.run("MATCH ()-[r]->() RETURN r").data()
# for i,j in zip(res,links):
#     print(i)
#     print(j)
#     print('\n')
# def getName(id):
#     result = graph.run("MATCH (r) WHERE id(r) = "+str(id)+ " RETURN r")
#     # print(result)
#     return type(result)
#
# print(getName(1))
