from src.RULBattery import logging 
from src.RULBattery.pipelines.pip_01_data_ingestion import DataIngestionPipeline


COMPONENT_01_NAME = "DATA_INGESTION COMPONENT"
try:

    logging.info(f"# ====================== {COMPONENT_01_NAME} Started! ================================= #")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.run()
    logging.info(f"## ======================== {COMPONENT_01_NAME} Terminated Successfully!======================= ##\n\nx******************x")

except Exception as e:
    logging.exception(e)
    raise e