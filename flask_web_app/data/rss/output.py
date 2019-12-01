"""Module contains objects related to printing data"""
import logging
from typing import Dict, Any

from flask import render_template

from data.conversion.html_converter import HtmlConverter
from data.conversion.pdf_converter import PdfConverter


class Output:
    """PrintData class"""

    @staticmethod
    def to_html_format(rss_feed_dict: Dict[str, Any]) -> None:
        """Output data to HTML file"""
        html_data = HtmlConverter(rss_feed_dict).convert_to_format()

        logging.info('Print RSS feed in HTML file')

        with open('./templates/news.html', 'w') as fw:
            fw.write(html_data)

    @staticmethod
    def to_pdf_format(rss_feed_dict: Dict[str, Any]) -> None:
        """Output data to PDF file"""

        PdfConverter(rss_feed_dict).convert_to_format()

        logging.info('Print RSS feed in PDF file')
