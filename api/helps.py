import collections
import logging
from collections import namedtuple
from enum import Enum

import asyncio
import aiohttp
import tqdm
import ujson
from aiohttp import web
from elasticsearch_dsl import Q


class ElasticSearchCourseHeaderService:
    """
    make elasticseach instance using document_class_name
    holds query_list, size and search_instance
    query_list:- list of query/keyword, on which summary will filter
    size:- length of filtered result
    """

    def __init__(self, document_class_name, query_list,size):
        self.query_list = query_list
        self.size =size
        self.search_instance = document_class_name.search()

    """ 
    filter summaries using query from given query list
    """
    def run_query_list(self):
        result = []
            # define elastic search query, where summary field must match with given query/keyword
        # q = Q('bool', must=[Q('multi_match', about=self.query_list[0]), fields=['about']])
        q = Q("multi_match", query=self.query_list[0], fields=['about'])
            # adding elastic search query,
            # sort filtered result based on _score,
            # result's length start from 0 to se    lf.size
        search_with_query = self.search_instance.query(q).sort('_score')[0:self.size]

            # execute elastic query
        response = search_with_query.execute()
        print (response)
        result.append(response.to_dict()['hits']['hits'])
        return result