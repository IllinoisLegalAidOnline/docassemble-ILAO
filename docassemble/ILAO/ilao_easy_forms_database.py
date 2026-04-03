import pandas
from docassemble.base.util import path_and_mimetype, get_language

__all__ = ['get_easy_forms_names', 'easy_forms_info']

easy_forms_info_by_name = {}
easy_forms_info_by_name_es = {}
easy_forms_names = []
easy_forms_names_es = []


def read_data(filename):
    the_xlsx_file, mimetype = path_and_mimetype(filename)  # pylint: disable=unused-variable
    df = pandas.read_excel(the_xlsx_file)
    for indexno in df.index:
        if not df['name'][indexno]:
            continue
        name_en = df['name'][indexno]
        name_es = df['name_es'][indexno] if 'name_es' in df.columns and pandas.notna(df['name_es'][indexno]) else name_en
        url = df['url'][indexno]
        
        easy_forms_names.append(name_en)
        easy_forms_info_by_name[name_en] = {"url": url}
        
        easy_forms_names_es.append(name_es)
        easy_forms_info_by_name_es[name_es] = {"url": url}


def get_easy_forms_names():
    if get_language() == 'es':
        return easy_forms_names_es
    return easy_forms_names


def easy_forms_info(easy_forms):
    # Check English names first, then Spanish names
    if easy_forms in easy_forms_info_by_name:
        return easy_forms_info_by_name[easy_forms]
    if easy_forms in easy_forms_info_by_name_es:
        return easy_forms_info_by_name_es[easy_forms]
    raise Exception("Reference to invalid Easy Form " + easy_forms)

read_data('docassemble.ILAO:data/sources/ilao_docassemble_easy_forms.xlsx')
