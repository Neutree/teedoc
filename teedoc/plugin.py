from .logger import Fake_Logger
import os

class Plugin_Base:
    name = "markdown-plugin"
    desc = "markdown plugin for teedoc"
    defautl_config = {
    }

    def __init__(self, config = {}, doc_src_path = ".", logger = None):
        '''
            @config a dict object
            @logger teedoc.logger.Logger object
        '''
        self.logger = Fake_Logger() if not logger else logger
        self.doc_src_path = doc_src_path
        

    def on_parse_files(self, files):
        '''
            result = {
                "ok": False,
                "msg": "",
                "htmls": {
                    "file1_path": {
                                    "title": "",
                                    "desc": "",
                                    "keywords": [],
                                    "body": html
                                 }
            }
        '''
        return None
    
    def on_parse_pages(self, pages):
        return None
    
    def on_add_html_header_items(self):
        return []
    
    def on_add_navbar_items(self):
        '''
            @return list items(navbar item, e.g. "<a href=></a>")
        '''
        return []
    
    def on_copy_files(self):
        '''
            copy file to out directory
            @return dict object, keyword is url, value is file path
                    {
                        "/static/css/theme-default.css": "{}/theme-default.css".format(assets_abs_path)
                    }
                    how to get assets_abs_path see teedoc-plugin-theme-default
        '''
        return {}

