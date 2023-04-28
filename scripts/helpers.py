from upsetplot import plot
from matplotlib import pyplot
from upsetplot import from_contents
from matplotlib import pyplot as plt
from upsetplot import UpSet

def to_1D(series):
 return pd.Series([x for _list in series for x in _list])

def add_list_to_dict(dict_variable = None, key = None, items_list = None):
  if key in dict_variable.keys():
    dict_variable[key].extend(items_list)
    dict_variable[key] = list(set(dict_variable[key]))
  else:
    dict_variable[key] = items_list
  return dict_variable

def plot_upset(items_dict : dict, element_size : float, color : str, output_name : str):
    data = from_contents(items_dict)
    fig = plt.figure()
    plot(data, fig=fig, 
        element_size=element_size, 
        show_counts = True,  
        facecolor=color, 
        sort_by = 'cardinality', 
        sort_categories_by='-cardinality')
    plt.savefig(f'../figures/{output_name}.pdf', bbox_inches='tight')