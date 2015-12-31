# coding: utf-8
import pandas as pd
import json
from elasticsearch import Elasticsearch


df = pd.read_csv('final-3.4.csv',low_memory=False)

tmp=df.to_json(orient = "records",date_format='iso')
df_json= json.loads(tmp)

es = Elasticsearch("localhost:9200")
maps = '{"mappings":{"txt":{"properties":{"CM-PCS":{"type":"string"},"CM-PCS-Name":{"type":"string","index":"not_analyzed"},"DRG":{"type":"string"},"DRG-NAME":{"type":"string","index":"not_analyzed"},"MDC":{"type":"string"},"RW":{"type":"double"},"上限臨界點":{"type":"double"},"下限臨界點":{"type":"double"},"個案數<20註記":{"type":"string"},"定額":{"type":"double"},"幾何平均住院日":{"type":"double"},"流水號":{"type":"double"}}}}}'
es.indices.create(index="twdrg34", body=maps)

for doc in df_json:
    #print doc
        es.index("twdrg34","txt",doc)
print "finished"

