import webbrowser
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape, Markup

# give jinja2 path to template.html dir
CUR_DIR = os.path.dirname(os.path.abspath(__file__))
fprintFilesDir = os.path.join(CUR_DIR, 'funPrint_files')
env = Environment(
    loader=FileSystemLoader(fprintFilesDir),
    autoescape=select_autoescape(['html', 'xml'])
)
env.filters['path_join'] = os.path.join


template = env.get_template('template.html')
outfile = os.path.join(fprintFilesDir, 'cp.html')

def funPrint(*args, spring=0.1, scale=1, net=False):

    if net is True:
        net = 'true'
    else:
        net = 'false'

    text = ' '.join(args)
    html = template.render(printText=Markup([text]), dir=fprintFilesDir, spring=spring, scale=scale, net=net)
    # TODO: see if it is bad to write files here
    with open(outfile, 'w') as f:
        f.write(html)
    webbrowser.open(outfile)
