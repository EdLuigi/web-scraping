from scrapy.pipelines.files import FilesPipeline

class CustomFilePipelines(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        if item.get('Title')[item.get('Title').find('.'):] == '.xlsx)':
            return item.get('Title')+'.xlsx'
        else:
            return item.get('Title')+'.pdf'
