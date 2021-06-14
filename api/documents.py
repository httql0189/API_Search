from elasticsearch_dsl import analyzer,Completion
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
my_analyzer = analyzer('my_analyzer',
                      tokenizer="letter",
                      filter=["lowercase"]
                     
                      )
# my_analyzer = analyzer('my_analyzer',
#     tokenizer=tokenizer('trigram', 'nGram', min_gram=3, max_gram=3),
#     filter=['lowercase']
# )
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
    #course_title= Completion()
    course_title = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='standard'),
            'suggest': fields.CompletionField(analyzer=my_analyzer),
            
            # 'tokenizer': fields.TextField(analyzer='letter'),
        }
     )

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
            # 'course_title',
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