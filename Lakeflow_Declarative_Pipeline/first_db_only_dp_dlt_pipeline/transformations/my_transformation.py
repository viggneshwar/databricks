from pyspark import pipelines as dp
@dp.table(name="lakehousecat1.deltadb.shipmentwe47")
def return_df():
    df1=spark.read.table("gcp_mysql_conn_we47.logistics.shipments1")
    return df1