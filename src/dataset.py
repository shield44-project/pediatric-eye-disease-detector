import pydicom

class PediatricDataset:

    def __init__(self, data_folder, label_file):
        # TODO: store paths
        pass


    def read_dicom(self, path):
        # TODO: read dicom file using pydicom
        pass


    def get_label(self, filename):
        # TODO: read label from csv
        pass


    def __len__(self):
        # TODO: return total images
        pass


    def __getitem__(self, index):
        # TODO: return image and label
        pass
