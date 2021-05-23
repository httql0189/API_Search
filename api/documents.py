from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl import (
    Document,
    fields,
    Index,
)

from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl.connections import connections

from .models import CourseHeader


# create the connection with ELASTICSEARCH server
connections.create_connection('qa',hosts=['localhost'], timeout=20)

# elastic_search analyzer setup
html_strip = analyzer('html_strip',
                      tokenizer="standard",
                      filter=["lowercase", "stop", "snowball"],
                      char_filter=["html_strip"]
                      )

@registry.register_document
class CourseHeaderDocument(Document):
    # course_image = fields.TextField(
    #     analyzer=html_strip,
    #     fields={'raw': fields.TextField(), }
    # )
    # about = fields.TextField(
    #     analyzer=html_strip,
    #     fields={'raw': fields.TextField(), }
    # )



    class Index:

        # Name of elastic_search index for Summaries model
        name = 'courseheader_data'

        # basic setup for elasticsearch
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:

        # the model name
        model = CourseHeader
        fields = [
            'course_url',
            'course_tag',
            'course_title',
            'rating',
            "about",
            'rating_count',
            'review_count',
            'offer_by',
            'enrolled',
            'skill_gain',
            'language',
            'subtitle',
            'course_image',
            'keyword'
            ]