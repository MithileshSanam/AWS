import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node source_catalog
source_catalog_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="orders", table_name="raw", transformation_ctx="source_catalog_node1"
)

# Script generated for node Change Schema
ChangeSchema_node1697020270682 = ApplyMapping.apply(
    frame=source_catalog_node1,
    mappings=[
        ("id", "long", "id", "int"),
        ("region", "string", "region", "string"),
        ("order_id", "long", "order_id", "string"),
    ],
    transformation_ctx="ChangeSchema_node1697020270682",
)

# Script generated for node sink_s3
sink_s3_node2 = glueContext.write_dynamic_frame.from_options(
    frame=ChangeSchema_node1697020270682,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://awslearning-bucket-2/parquet_output/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="sink_s3_node2",
)

job.commit()
