
import pandas as pd
from sodapy import Socrata


def get_dataset_sdo():
    print("Starting to download dataset from www.dati.lombardia.it")
    client = Socrata("www.dati.lombardia.it", None)
    results = client.get("jv9t-c6q6")
    print("Download completed")
    dictionary_dataset = manipulate_data_json(results)
    print(dictionary_dataset)
    data_file = pd.DataFrame.from_dict(dictionary_dataset)
    data_file.to_csv(r'datasetSDO.csv', index=False, header=True)
    print(f'Created datasetSDO.csv')


def manipulate_data_json(results):
    dictionary_keys = results[0].keys()
    dictionary_dataset = dict()
    for key in dictionary_keys:
        if key != 'posizione_ats' and not ('computed_region' in key):
            dictionary_dataset[key] = []
            for element in results:
                if key in element:
                    dictionary_dataset[key].append(element[key])
                else:
                    dictionary_dataset[key].append("")
    return dictionary_dataset


def get_dataset_filtered_sdo():
    print("Starting to download dataset from www.dati.lombardia.it")
    client = Socrata("www.dati.lombardia.it", None)
    results = client.get("mpng-nv6x")
    print("Download completed")
    dictionary_dataset = manipulate_data_json(results)
    print(dictionary_dataset)
    data_file = pd.DataFrame.from_dict(dictionary_dataset)
    data_file.to_csv(r'datasetSDO_Filtered.csv', index=False, header=True)
    print(f'Created datasetSDO_Filtered.csv')


def main():
    get_dataset_sdo()
    get_dataset_filtered_sdo()



if __name__ == '__main__':
    main()

