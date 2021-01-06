import json

html = ""
self_close_tag = ['source', 'param', 'meta', 'link', 'input', 'img', 'hr', 'br']


def html_source(tag, att, nested):
    global html
    html += "<" + tag
    if isinstance(att, dict) and len(att) != 0:
        # html += ' style="'
        for property, value in att.items():
            html += ' ' + '{}="{}"'.format(property, value)
        # html +=' '
    if tag in self_close_tag:

        html += '/>\n'
    else:
        html += '>\n'
    if (isinstance(nested, list)):
        for element in nested:
            if (isinstance(element, dict)):
                spliting_data(element)
            else:
                html += str(element)
    elif (isinstance(nested, str)):
        html += nested
    if not (tag in self_close_tag):
        html += "</" + str(tag) + ">" + '\n'


def spliting_data(data):
    tag_name = data.pop('tag_name')
    try:
        nested = data.pop('nested_element')
    except:
        nested = None
    attribute = data
    html_source(tag_name, attribute, nested)


with open('portfolio.json', 'r') as f:
    data = json.load(f)
    spliting_data(data)
print(html)
with open('index_out.html', 'w') as index:
    index.write(html)
