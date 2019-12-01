"""Module contains objects related to logs"""
import logging
from typing import Dict, Any

from data.rss.data_loader import DataLoader
from data.rss.output import Output
from data.rss.rss_feed import RSSFeed
from data.db.mongodb import MongoDatabase
from data.db.mongodb_config import HOST, PORT, DB_NAME, COLLECTION_NAME


class Application:
    """Application class"""
    def __init__(self, dict_args):
        """Init Application class"""
        self.dict_args: Dict[str, Any] = dict_args

    def run_app(self) -> None:
        """Мethod sets application behavior"""

        logging.info(f'args{self.dict_args}')
        
        mongo_db = MongoDatabase(HOST, PORT, DB_NAME, COLLECTION_NAME)
        mongo_db.database_connection()
        mongo_db.kek(self.dict_args)

        if self.dict_args['source'] is not None:

            data = DataLoader(self.dict_args['source']).upload()

            feed = RSSFeed(self.dict_args, data)

            process_data = feed.data_processing()

            mongo_db.cache_news_feed(process_data)

            news = mongo_db.get_news(self.dict_args["limit"], self.dict_args["date"], self.dict_args["source"])

            if news is not None:

                if self.dict_args["to_pdf"]:
                    Output.to_pdf_format(news)

            Output.to_html_format(news)
