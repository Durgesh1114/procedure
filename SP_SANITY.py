def EP_SSOT_BTCH_SP_SANITY(SQUD_NM,KPI_CHCK):
    class No_data_found(Exception):
        def __init__(self):
            super()
    try:
        df = spark.sql(""" SELECT CHCK_QERY FROM EP_SSOT_CNTL_TECH_VIEW.SANITY_REPORT WHERE SQUD_NM = {} AND 
            KPI_CHCK = {}""".format(SQUD_NM,KPI_CHCK))
        if df.count() == 0:
            raise No_data_found
        df.createOrReplaceTempView("RSLT")
        v_count = spark.sql("""select * from RSLT""").count()
        for i in range(0,v_count):
            v_CHCK_QERY = spark.sql("""SELECT CHCK_QERY FROM RSLT""").collect()[i][0]
            spark.sql("{}""".format(v_CHCK_QERY)).show()
        return "success"

    except No_data_found:
        print("No Data found to in table EP_SSOT_CNTL_TECH_VIEW.SANITY_REPORT for the parameters")
