import yaml


class Config:
    def __init__(self, data):
        self.data = data
        self.host = self.load_host()
        self.port = self.load_port()
        self.encoding = self.load_encoding()

    def load_host(self):
        return self.data["info"]["host"]

    def load_port(self):
        return self.data["info"]["port"]

    def load_encoding(self):
        return self.data["encoding"]


def read_config_data():
    with open('yamlpy.yml', 'r') as stream:
        data = yaml.safe_load_all(stream)
        data_listed = list(data)[0]
    return data_listed
